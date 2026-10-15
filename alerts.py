import os
import json
import time
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "alert_config.json"

DEFAULT_CONFIG = {
    "enabled": True,
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "",
    "sender_password": "",
    "receiver_email": "",
    "cooldown_seconds": 30,
    "attach_image": True
}

# In-memory record of last sent alert timestamp to prevent flooding
_last_alert_time = 0

def load_alert_config():
    """Load alert configuration from disk or create default."""
    if not CONFIG_FILE.exists():
        save_alert_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            config = DEFAULT_CONFIG.copy()
            config.update(data)
            return config
    except Exception as e:
        print(f"[Alerts] Error loading config: {e}")
        return DEFAULT_CONFIG.copy()

def save_alert_config(config):
    """Save alert configuration to disk."""
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        print(f"[Alerts] Error saving config: {e}")
        return False

def is_configured(config=None):
    """Check if necessary SMTP credentials are provided."""
    if config is None:
        config = load_alert_config()
    sender = config.get("sender_email", "").strip()
    pwd = config.get("sender_password", "").strip()
    receiver = config.get("receiver_email", "").strip()
    return bool(sender and pwd and receiver)

def build_email_html(violations, counts, compliance_score, status, timestamp_str):
    """Generate modern, rich HTML email body for PPE safety violation alert."""
    badge_color = "#ef4444" if status == "CRITICAL" else "#f59e0b"
    
    violation_rows = "".join([
        f"<li style='margin-bottom: 8px; color: #b91c1c; font-weight: 500;'>⚠️ {v}</li>"
        for v in violations
    ])
    
    count_rows = "".join([
        f"<tr><td style='padding: 6px 12px; border-bottom: 1px solid #e2e8f0; text-transform: capitalize;'>{cls_name}</td>"
        f"<td style='padding: 6px 12px; border-bottom: 1px solid #e2e8f0; font-weight: bold;'>{cnt}</td></tr>"
        for cls_name, cnt in counts.items() if cnt > 0
    ])

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f1f5f9; margin: 0; padding: 20px; }}
        .card {{ max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); border: 1px solid #e2e8f0; }}
        .header {{ background: linear-gradient(135deg, #1e293b, #0f172a); color: #ffffff; padding: 24px; text-align: center; }}
        .header h1 {{ margin: 0; font-size: 22px; letter-spacing: -0.5px; }}
        .header p {{ margin: 6px 0 0 0; color: #94a3b8; font-size: 14px; }}
        .content {{ padding: 24px; color: #334155; }}
        .status-badge {{ display: inline-block; padding: 6px 14px; border-radius: 9999px; background-color: {badge_color}; color: white; font-weight: 700; font-size: 13px; margin-bottom: 16px; letter-spacing: 0.5px; }}
        .alert-box {{ background-color: #fef2f2; border-left: 4px solid #ef4444; padding: 14px 18px; border-radius: 4px; margin-bottom: 20px; }}
        .alert-box h3 {{ margin: 0 0 8px 0; color: #991b1b; font-size: 16px; }}
        .alert-box ul {{ margin: 0; padding-left: 20px; }}
        .table-section {{ margin-top: 20px; }}
        .table-section table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
        .table-section th {{ text-align: left; background-color: #f8fafc; padding: 8px 12px; color: #64748b; font-size: 12px; text-transform: uppercase; border-bottom: 2px solid #e2e8f0; }}
        .footer {{ background: #f8fafc; padding: 16px; text-align: center; color: #94a3b8; font-size: 12px; border-top: 1px solid #e2e8f0; }}
      </style>
    </head>
    <body>
      <div class="card">
        <div class="header">
          <h1>🛡️ PPEGuard Safety Alert</h1>
          <p>Workplace PPE Compliance Monitoring System</p>
        </div>
        <div class="content">
          <span class="status-badge">STATUS: {status}</span>
          <div style="float: right; font-size: 13px; color: #64748b; margin-top: 6px;">
            Compliance: <strong>{compliance_score}%</strong>
          </div>
          
          <div class="alert-box">
            <h3>⚠️ Violations Detected ({timestamp_str})</h3>
            <ul>
              {violation_rows}
            </ul>
          </div>
          
          <div class="table-section">
            <h4 style="margin: 0 0 10px 0; color: #1e293b; font-size: 14px;">Detection Summary</h4>
            <table>
              <thead>
                <tr>
                  <th>Object / Gear</th>
                  <th>Count</th>
                </tr>
              </thead>
              <tbody>
                {count_rows}
              </tbody>
            </table>
          </div>
          
          <p style="margin-top: 24px; font-size: 13px; color: #64748b;">
            An annotated detection image highlighting individuals without required protective equipment has been attached to this email. Immediate safety supervisor action is advised.
          </p>
        </div>
        <div class="footer">
          PPEGuard Automated Safety Monitoring &bull; Generated at {timestamp_str}
        </div>
      </div>
    </body>
    </html>
    """
    return html

def send_email_alert(violations, counts, compliance_score, status, image_path=None, force=False):
    """
    Send an email alert to the configured recipient.
    Returns (success: bool, message: str)
    """
    global _last_alert_time
    config = load_alert_config()
    
    if not config.get("enabled", True) and not force:
        return False, "Alerts are disabled in configuration."
        
    if not is_configured(config):
        return False, "SMTP settings not configured. Please set sender/receiver credentials."
        
    # Rate limit check
    cooldown = config.get("cooldown_seconds", 30)
    now = time.time()
    if not force and (now - _last_alert_time) < cooldown:
        remaining = int(cooldown - (now - _last_alert_time))
        return False, f"Alert rate-limited. Cooldown active ({remaining}s remaining)."
        
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subject = f"🚨 [PPEGuard Alert] {status}: Safety Violations Detected ({timestamp_str})"
    
    sender_email = config.get("sender_email", "").strip()
    # Handle passwords that contain spaces (like Google App Passwords)
    sender_pwd = config.get("sender_password", "").replace(" ", "").strip()
    receiver_email = config.get("receiver_email", "").strip()
    smtp_server = config.get("smtp_server", "smtp.gmail.com").strip()
    smtp_port = int(config.get("smtp_port", 587))

    # Create message
    msg = MIMEMultipart("related")
    msg["Subject"] = subject
    msg["From"] = f"PPEGuard Safety System <{sender_email}>"
    msg["To"] = receiver_email
    
    # HTML content
    html_body = build_email_html(violations, counts, compliance_score, status, timestamp_str)
    msg.attach(MIMEText(html_body, "html"))
    
    # Attach image if available and configured
    if config.get("attach_image", True) and image_path and os.path.exists(image_path):
        try:
            with open(image_path, "rb") as img_f:
                img_data = img_f.read()
                img_part = MIMEImage(img_data, name=os.path.basename(image_path))
                img_part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_path))
                msg.attach(img_part)
        except Exception as e:
            print(f"[Alerts] Could not attach image: {e}")

    # Dispatch via SMTP
    try:
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=15)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, sender_pwd)
        server.send_message(msg)
        server.quit()
        
        _last_alert_time = time.time()
        print(f"[Alerts] Successfully sent alert email to {receiver_email}")
        return True, f"Alert email sent to {receiver_email}"
    except Exception as e:
        err_msg = str(e)
        print(f"[Alerts] SMTP Error: {err_msg}")
        return False, f"Failed to send email: {err_msg}"

def trigger_async_alert(violations, counts, compliance_score, status, image_path=None):
    """Fire and forget alert in a background thread to prevent blocking web requests."""
    t = threading.Thread(
        target=send_email_alert,
        args=(violations, counts, compliance_score, status, image_path, False),
        daemon=True
    )
    t.start()
