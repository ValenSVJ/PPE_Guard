import os
import uuid
import torch
from pathlib import Path
from flask import Flask, request, jsonify, render_template, url_for
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import alerts

app = Flask(__name__)

# Security and Paths
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / 'static' / 'uploads'
RESULT_FOLDER = BASE_DIR / 'static' / 'results'

app.config['UPLOAD_FOLDER'] = str(UPLOAD_FOLDER)
app.config['RESULT_FOLDER'] = str(RESULT_FOLDER)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

# Model Path Resolution (prioritizes 100-epoch model, falls back to train-4)
MODEL_CANDIDATES = [
    BASE_DIR / "runs" / "detect" / "train-100" / "weights" / "best.pt",
    BASE_DIR / "runs" / "detect" / "train-4" / "weights" / "best.pt",
    BASE_DIR / "yolo26n.pt"
]
MODEL_PATH = next((p for p in MODEL_CANDIDATES if p.exists()), MODEL_CANDIDATES[1])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Setup Device and Load Model
def setup_device_and_model():
    device = 0 if torch.cuda.is_available() else "cpu"
    gpu_name = "N/A"
    
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
    
    print(f"Loading model to device: {device} (GPU: {gpu_name})")
    print(f"Model Path: {MODEL_PATH}")
    try:
        model = YOLO(str(MODEL_PATH))
        model.to(device)
        print("Model Classes:", model.names)
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None
        
    return model, device, gpu_name

# Initialize model once on startup
print("Initializing PPEGuard...")
model, device, gpu_name = setup_device_and_model()

@app.route('/')
def index():
    return render_template('index.html', 
                           gpu_name=gpu_name, 
                           device=device,
                           cuda_available=torch.cuda.is_available())

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'success': False, 'error': 'Model not loaded.'}), 500
        
    if 'image' not in request.files:
        return jsonify({'success': False, 'error': 'No image provided.'}), 400
        
    file = request.files['image']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'Empty file submitted.'}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # add uuid to prevent conflicts
        unique_id = str(uuid.uuid4())[:8]
        filename = f"{unique_id}_{filename}"
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Run inference explicitly on correct device
            with torch.no_grad():
                results = model.predict(source=filepath, device=device, conf=0.25, verbose=False)
            
            if len(results) > 0:
                result = results[0]
                
                # Save annotated image
                annotated_img_name = f"result_{filename}"
                annotated_img_path = os.path.join(app.config['RESULT_FOLDER'], annotated_img_name)
                result.save(filename=annotated_img_path)
                
                # Process detections dynamically using model.names
                detections = []
                counts = {name: 0 for name in model.names.values()}
                total_conf = 0.0
                
                for box in result.boxes:
                    cls_id = int(box.cls[0].item())
                    conf = float(box.conf[0].item())
                    cls_name = model.names[cls_id]
                    
                    counts[cls_name] = counts.get(cls_name, 0) + 1
                    total_conf += conf
                    
                    detections.append({
                        'class': cls_name,
                        'confidence': round(conf * 100, 1),
                        'bbox': [round(x, 1) for x in box.xyxy[0].tolist()]
                    })
                
                num_detections = len(detections)
                avg_conf = round((total_conf / num_detections) * 100, 1) if num_detections > 0 else 0
                
                # Comprehensive PPE Compliance & Violation Logic
                people = counts.get('Person', 0)
                helmets = counts.get('helmet', 0)
                vests = counts.get('vest', 0)
                
                compliance_score = 100
                violations = []
                
                # Check negative explicit classes
                negative_gear_map = {
                    'no_helmet': 'Hard Hat / Helmet',
                    'no_vest': 'Reflective Safety Vest',
                    'no_goggle': 'Eye Protection / Goggles',
                    'no_gloves': 'Safety Gloves',
                    'no_boots': 'Safety Boots',
                    'none': 'Protective Equipment (No Gear Detected)'
                }
                
                for neg_cls, label in negative_gear_map.items():
                    cnt = counts.get(neg_cls, 0)
                    if cnt > 0:
                        penalty = 15 * cnt
                        compliance_score = max(0, compliance_score - penalty)
                        violations.append(f"Direct violation: {cnt} instance(s) of {neg_cls} ({label} missing).")
                
                if people > 0:
                    helmet_ratio = min(1.0, helmets / people)
                    vest_ratio = min(1.0, vests / people)
                    compliance_score = round(min(compliance_score, ((helmet_ratio + vest_ratio) / 2) * 100), 1)
                    
                    if helmets < people:
                        violations.append(f"Missing Helmets: Found {helmets} for {people} Persons.")
                    if vests < people:
                        violations.append(f"Missing Vests: Found {vests} for {people} Persons.")
                    if helmets == 0 and vests == 0:
                        violations.append("CRITICAL: Person detected with NO protective gear!")
                
                status = "SAFE"
                if len(violations) > 0:
                    if compliance_score < 70 or any(counts.get(k, 0) > 0 for k in negative_gear_map):
                        status = "CRITICAL"
                    else:
                        status = "WARNING"

                # Process Automated Safety Email Alert
                alert_config = alerts.load_alert_config()
                alert_info = {
                    'triggered': False,
                    'enabled': alert_config.get('enabled', True),
                    'configured': alerts.is_configured(alert_config),
                    'recipient': alert_config.get('receiver_email', ''),
                    'message': 'No safety violations detected.'
                }
                
                if len(violations) > 0:
                    alert_info['triggered'] = True
                    if not alert_config.get('enabled', True):
                        alert_info['message'] = 'Alert disabled in system settings.'
                    elif not alert_info['configured']:
                        alert_info['message'] = 'Violation detected! Email alert skipped (SMTP credentials not yet configured).'
                    else:
                        alerts.trigger_async_alert(violations, counts, compliance_score, status, annotated_img_path)
                        alert_info['message'] = f"Violation detected! Alert email dispatched to {alert_config.get('receiver_email')}."
                
                return jsonify({
                    'success': True,
                    'annotated_image': url_for('static', filename=f'results/{annotated_img_name}'),
                    'detections': detections,
                    'counts': counts,
                    'average_confidence': avg_conf,
                    'compliance_score': compliance_score,
                    'status': status,
                    'violations': violations,
                    'alert': alert_info,
                    'device': str(device)
                })
            else:
                return jsonify({'success': False, 'error': 'No results returned from model.'}), 500
                
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500
            
    return jsonify({'success': False, 'error': 'Invalid file type.'}), 400

@app.route('/api/alerts/config', methods=['GET', 'POST'])
def handle_alert_config():
    if request.method == 'GET':
        cfg = alerts.load_alert_config()
        sanitized = cfg.copy()
        sanitized['has_password'] = bool(cfg.get('sender_password'))
        sanitized['sender_password'] = '******' if cfg.get('sender_password') else ''
        return jsonify({'success': True, 'config': sanitized, 'is_configured': alerts.is_configured(cfg)})
    else:
        data = request.get_json() or {}
        current_cfg = alerts.load_alert_config()
        # If user preserved '******', do not overwrite existing password
        if data.get('sender_password') == '******':
            data['sender_password'] = current_cfg.get('sender_password', '')
            
        for key in ['enabled', 'smtp_server', 'smtp_port', 'sender_email', 'sender_password', 'receiver_email', 'cooldown_seconds', 'attach_image']:
            if key in data:
                current_cfg[key] = data[key]
                
        success = alerts.save_alert_config(current_cfg)
        return jsonify({
            'success': success, 
            'is_configured': alerts.is_configured(current_cfg),
            'message': 'Alert configuration saved.'
        })

@app.route('/api/alerts/test', methods=['POST'])
def test_alert():
    data = request.get_json() or {}
    cfg = alerts.load_alert_config()
    
    # Allow testing with submitted form values directly
    for key in ['smtp_server', 'smtp_port', 'sender_email', 'sender_password', 'receiver_email']:
        if key in data and data[key] and data[key] != '******':
            cfg[key] = data[key]
            
    if not alerts.is_configured(cfg):
        return jsonify({
            'success': False, 
            'message': 'Cannot test: sender email, password, and receiver email must all be filled.'
        }), 400

    # Temporarily persist if user tested new working fields
    alerts.save_alert_config(cfg)
    
    test_violations = ["TEST ALERT: Worker detected in hazardous zone with NO protective gear (Helmet & Vest missing)."]
    test_counts = {"Person": 1, "no_helmet": 1, "no_vest": 1}
    success, msg = alerts.send_email_alert(
        violations=test_violations,
        counts=test_counts,
        compliance_score=0,
        status="CRITICAL",
        image_path=None,
        force=True
    )
    return jsonify({'success': success, 'message': msg})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
