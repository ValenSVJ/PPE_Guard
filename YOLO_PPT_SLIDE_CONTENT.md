# PowerPoint Slide Content: PPEGuard Presentation Deck

**Project Title:** PPEGuard — AI Workplace Safety & PPE Compliance Monitoring System  
**Presentation Target:** College-Level Technical Presentation / Engineering Capstone Defense  
**Slide Count:** 20 Structured Slides  

---

### Slide 1: Title Slide
- **Slide Number:** 1
- **Slide Title:** PPEGuard: AI-Powered Workplace Safety & PPE Compliance Monitoring System
- **Presentation Content:**
  - **Subtitle:** An Automated Computer Vision System for Real-Time Hazard Detection and Safety Auditing
  - **Core Frameworks:** Ultralytics YOLO26 Nano & Flask Web Architecture
  - **Domain:** Data Science | Computer Vision | Deep Learning | Industrial Safety IoT
  - **Presenter:** [Student Name / Group Members]
  - **Department:** Department of Computer Engineering / Data Science
  - **Date:** Academic Year 2026
- **Suggested Visual:**
  - Split banner visual: Left side showing the PPEGuard logo shield; right side showing an example site inspection photo with bounding boxes around hard hats, high-vis vests, and workers (`ppe-inference-im0.png`).
- **Speaker Notes:**
  > "Good morning, respected professors, evaluators, and colleagues. Today, I am presenting our Data Science capstone project titled 'PPEGuard: AI-Powered Workplace Safety & PPE Compliance Monitoring System.' In this project, we address industrial safety hazards by developing an automated deep learning pipeline that detects personal protective equipment, calculates compliance scores mathematically, and dispatches automated email alerts when violations are observed."

---

### Slide 2: Introduction & Domain Context
- **Slide Number:** 2
- **Slide Title:** Introduction: The Crucial Role of PPE in Workplace Safety
- **Presentation Content:**
  - **Industrial Reality:** Heavy construction, mining, and manufacturing represent hazardous working environments.
  - **The Safety Barrier:** Personal Protective Equipment (PPE)—hard hats, high-visibility vests, gloves, boots, and goggles—serves as the primary line of defense against workplace injury and fatalities.
  - **Regulatory Framework:** Compliance is legally mandated by bodies such as OSHA and ISO 45001.
  - **The Human Element:** Despite strict policies, human error, discomfort, and negligence lead to frequent non-compliance and preventable accidents.
- **Suggested Visual:**
  - Infographic depicting OSHA's "Fatal Four" construction hazards (Falls, Struck-By, Electrocution, Caught-in/between) alongside icons of essential protective equipment (helmet, vest, gloves, boots, goggles).
- **Speaker Notes:**
  > "Construction sites and heavy industries are unpredictable environments. Across the world, regulatory organizations like OSHA mandate the continuous use of PPE. However, statistics show that the vast majority of severe injuries occur simply because workers momentarily take off their hard hats or reflective vests. Ensuring continuous compliance across hundreds of workers on active job sites is the central challenge we are solving."

---

### Slide 3: Problem Statement
- **Slide Number:** 3
- **Slide Title:** Problem Statement: The Limits of Manual Safety Monitoring
- **Presentation Content:**
  - **Unmonitored Blind Spots:** Vast job sites cannot be covered simultaneously by safety inspectors.
  - **Human Fatigue & Subjectivity:** Safety auditors experience cognitive fatigue, resulting in inconsistent enforcement and missed violations.
  - **Passive CCTV Infrastructure:** Standard surveillance cameras merely record video footage for post-accident investigations rather than active prevention.
  - **Delayed Hazard Intervention:** By the time a supervisor notices a worker entering a hazardous zone without a helmet, an incident may already have occurred.
- **Suggested Visual:**
  - Comparison graphic: A traditional safety officer checking a clipboard on a chaotic construction site vs. an automated camera lens overlay with warning markers.
- **Speaker Notes:**
  > "Current site monitoring relies almost entirely on manual safety walks. An inspector can only be in one place at a time, and surveillance cameras currently act as passive digital witnesses—recording footage that is reviewed only after a tragedy occurs. There is an urgent need for an automated system that detects infractions the moment they happen and instantly notifies supervisors."

---

### Slide 4: Existing System vs. Proposed Solution
- **Slide Number:** 4
- **Slide Title:** Existing Approaches vs. The PPEGuard Paradigm
- **Presentation Content:**
  | Operational Metric | Traditional Inspection | Passive CCTV | PPEGuard (Proposed) |
  | :--- | :--- | :--- | :--- |
  | **Monitoring Mode** | Periodic spot-checks | Continuous passive recording | Continuous intelligent analysis |
  | **Reaction Time** | Hours to days | Post-incident review only | Near real-time (< 1 second) |
  | **Alert Mechanism** | Verbal / Manual | None | Automated SMTP email alerts |
  | **Scoring Consistency** | Subjective | None | Objective mathematical scoring (0–100%) |
  | **Visual Evidence** | None / Manual photos | Uncut video logs | Annotated bounding box evidence |
- **Suggested Visual:**
  - Comparative flow diagram showing: (Old Way: Incident -> Injury -> Video Review) vs. (Proposed Way: Detection -> Rule Evaluation -> Immediate Alert -> Intervention).
- **Speaker Notes:**
  > "This comparison highlights the fundamental shift PPEGuard introduces. Traditional systems either rely on periodic human spot-checks or passive recording. PPEGuard converts raw imagery into actionable safety intelligence within seconds, delivering objective scores and automated alerts directly to supervisors."

---

### Slide 5: Project Objectives
- **Slide Number:** 5
- **Slide Title:** Project Objectives & Research Scope
- **Presentation Content:**
  - **Primary Objective:** Build an end-to-end computer vision and web-based monitoring platform that detects PPE compliance and automates hazard alerting.
  - **Technical Objectives:**
    1. Adapt and fine-tune the Ultralytics YOLO26 Nano architecture on an 11-class safety dataset.
    2. Engineer a rule-based compliance algorithm that checks person-to-gear ratios and penalizes missing equipment.
    3. Implement an asynchronous, non-blocking email alert system with annotated image attachments.
    4. Build a responsive dark-mode dashboard for user interaction, file ingestion, and hardware reporting.
    5. Evaluate detection precision, recall, and mAP to validate real-world applicability.
- **Suggested Visual:**
  - Circular objective flow: [Dataset & Fine-Tuning] -> [YOLO Inference] -> [Compliance Scoring] -> [Async Alert Dispatch] -> [Web Dashboard].
- **Speaker Notes:**
  > "Our project is guided by five clear technical objectives: first, training a state-of-the-art YOLO model; second, developing an explainable compliance algorithm; third, integrating an asynchronous alerting engine; fourth, delivering a modern user interface; and finally, evaluating our model against rigorous data science metrics."

---

### Slide 6: Complete Technology Stack
- **Slide Number:** 6
- **Slide Title:** Technical Stack & Architecture Foundation
- **Presentation Content:**
  - **Core Programming:** Python (v3.10–3.13) for backend logic; JavaScript (ES6+) for dynamic UI interactions.
  - **Deep Learning Framework:** PyTorch (v2.x) with CUDA hardware acceleration.
  - **Object Detection Engine:** Ultralytics YOLO26 Nano (`YOLO26n`) architecture.
  - **Web Application Framework:** Flask (v3.x) RESTful server and template engine.
  - **Networking & Protocols:** SMTP over TLS (`smtplib`), RFC 2822 MIME multipart attachments, browser Fetch API.
  - **Concurrency:** Multi-threaded execution (`threading.Thread`) for non-blocking email delivery.
  - **UI/UX Design:** Semantic HTML5 and Vanilla CSS3 (glassmorphism dark-theme with zero heavy UI dependencies).
- **Suggested Visual:**
  - Technology logo grid showing: Python, PyTorch, Ultralytics YOLO, Flask, JavaScript, HTML5/CSS3, and Gmail SMTP.
- **Speaker Notes:**
  > "Here is our complete technology stack. We chose Python and PyTorch for our deep learning pipeline, paired with Ultralytics for YOLO execution. Our backend is powered by Flask, running on a multi-threaded architecture that handles web requests and email alerts in parallel. The frontend is built using pure Vanilla CSS and JavaScript, keeping the application lightweight, fast, and free of bulky external frameworks."

---

### Slide 7: Dataset Overview: Construction-PPE
- **Slide Number:** 7
- **Slide Title:** Dataset Analysis: Construction-PPE Benchmark
- **Presentation Content:**
  - **Dataset Source:** Official Ultralytics Construction-PPE Dataset (under AGPL-3.0 License).
  - **Total Volume:** **1,416 annotated images** distributed across three canonical splits:
    - **Training Set:** 1,132 images (80.0%)
    - **Validation Set:** 143 images (10.1%)
    - **Testing Set:** 141 images (9.9%)
  - **Annotation Format:** Standard YOLO Darknet format (`.txt` files with normalized coordinates `class x y w h`).
  - **Data Augmentation Pipeline:**
    - Mosaic Augmentation ($1.0$, closed in final 10 epochs)
    - Albumentations: Blur, MedianBlur, CLAHE, ToGray
    - Color Jitter (HSV) & Horizontal Flips (`fliplr=0.5`)
- **Suggested Visual:**
  - Split bar chart displaying the 80/10/10 dataset split alongside sample annotated bounding box images from the dataset (`train_batch0.jpg` or `labels.jpg` from the project run).
- **Speaker Notes:**
  > "For training and validation, we utilized the Ultralytics Construction-PPE dataset. It contains 1,416 images partitioned into an 80-10-10 split for training, validation, and testing. Every image is annotated in standard YOLO Darknet format. During training, we applied extensive data augmentation—including mosaic composition, CLAHE contrast enhancement, and color jittering—to make our model resilient to harsh outdoor lighting and shadowed conditions."

---

### Slide 8: The 11 Target Detection Classes
- **Slide Number:** 8
- **Slide Title:** Detection Taxonomy: Positive vs. Negative Classes
- **Presentation Content:**
  - **Dual-Perspective Class Design:** Unlike standard detectors that only identify gear, this dataset trains the model on both positive compliance and explicit violations:
  - **1. Subject Class:**
    - `Person` (Class 6): Human presence detection.
  - **2. Positive PPE Classes (Compliant):**
    - `helmet` (Class 0), `vest` (Class 2), `gloves` (Class 1), `boots` (Class 3), `goggles` (Class 4).
  - **3. Explicit Negative Classes (Violations):**
    - `no_helmet` (Class 7), `no_vest` (Class 8), `no_gloves` (Class 9), `no_boots` (Class 10), `no_goggle` (Class 8), `none` (Class 5).
- **Suggested Visual:**
  - A two-column table or card visual contrasting: Green badges for positive gear (`helmet`, `vest`, `boots`) vs. Red hazard badges for explicit negative classes (`no_helmet`, `no_vest`, `none`).
- **Speaker Notes:**
  > "A unique strength of our dataset is its dual-perspective taxonomy across 11 classes. It doesn't just detect if a helmet or vest is present; it also includes dedicated negative classes like 'no_helmet' and 'no_vest'. This allows our deep learning model to explicitly recognize when a worker's head is exposed without protection, significantly reducing false compliance assumptions."

---

### Slide 9: YOLO26 Model Architecture
- **Slide Number:** 9
- **Slide Title:** Deep Learning Architecture: Ultralytics YOLO26 Nano
- **Presentation Content:**
  - **Architecture Footprint:**
    - 260 layers, 2.508 million parameters, 5.9 GFLOPs (fused: 122 layers, 5.3 GFLOPs).
    - Compact disk storage: ~5.39 MB weights file (`best.pt`).
  - **Backbone Network:**
    - Strided convolutions for progressive downsampling ($3 \to 16 \to 32 \to 64 \to 128 \to 256$ channels).
    - `C3k2` Cross Stage Partial blocks for efficient gradient propagation.
    - `SPPF` (Spatial Pyramid Pooling) and `C2PSA` (Pointwise Spatial Attention).
  - **Neck Network:**
    - Path Aggregation Feature Pyramid Network (PAN-FPN) fusing multi-scale feature maps.
  - **Head Network:**
    - Anchor-free decoupled head outputting predictions across three grid scales ($80 \times 80$, $40 \times 40$, $20 \times 20$).
- **Suggested Visual:**
  - Clean architectural block diagram displaying Backbone -> PAN-FPN Neck -> Decoupled Detection Head -> Non-Maximum Suppression (NMS).
- **Speaker Notes:**
  > "Let's examine our neural network architecture. We selected Ultralytics YOLO26 Nano. With just 2.5 million parameters and a 5.39 MB model file, it provides exceptional computational efficiency without sacrificing accuracy. It features a modern backbone with Cross-Stage Partial blocks and Spatial Attention, a multi-scale Feature Pyramid neck, and an anchor-free decoupled head that predicts bounding boxes and classes across three distinct spatial scales."

---

### Slide 10: System Architecture & Data Pipeline
- **Slide Number:** 10
- **Slide Title:** High-Level System Architecture
- **Presentation Content:**
  - **1. Client Tier:** Web Browser UI (`templates/index.html`) submitting images via Fetch API.
  - **2. Application Tier:** Flask Backend (`app.py`) managing file ingestion and secure storage.
  - **3. Deep Learning Vision Tier:** PyTorch YOLO engine executing forward passes and saving annotated visual results.
  - **4. Safety & Compliance Engine:** Mathematical rule evaluation calculating scores and assigning risk status.
  - **5. Notification Tier:** Asynchronous daemon thread (`alerts.py`) dispatching TLS SMTP emails with attached evidence.
- **Suggested Visual:**
  - System architecture diagram showing the five tiers and the directional data flow arrows from image upload to email inbox.
- **Speaker Notes:**
  > "This diagram illustrates the complete system architecture across five tiers. The client submits an image through our web portal. Flask receives the file, assigns a unique UUID, and passes it to the YOLO vision engine. Once detections are generated, our compliance engine evaluates safety scores. If any safety violations exist, an asynchronous background thread fires, packaging the results into an email alert while the user instantly receives visual feedback on their screen."

---

### Slide 11: Compliance Scoring & Risk Assessment Algorithm
- **Slide Number:** 11
- **Slide Title:** Rule-Based Safety Compliance Algorithm
- **Presentation Content:**
  - **Mathematical Formulation:**
    1. **Negative Detection Penalty:**
       $$\text{Base Score} = \max(0, \, 100 - (15 \times \text{negative\_instances}))$$
    2. **Person-to-Gear Ratio Calculation:**
       $$\text{Helmet Ratio} = \min\left(1.0, \, \frac{\text{helmets}}{\text{people}}\right), \quad \text{Vest Ratio} = \min\left(1.0, \, \frac{\text{vests}}{\text{people}}\right)$$
       $$\text{Final Compliance Score} = \text{round}\left(\min\left(\text{Base Score}, \, \frac{\text{Helmet Ratio} + \text{Vest Ratio}}{2} \times 100\right), \, 1\right)$$
  - **Three-Tier Operational Status:**
    - **`SAFE` (Green):** 100% compliance, zero negative detections.
    - **`WARNING` (Amber):** Compliance $\ge 70\%$ with minor missing gear.
    - **`CRITICAL` (Red):** Compliance $< 70\%$, explicit negative classes detected, or persons with zero gear.
- **Suggested Visual:**
  - Color-coded flowchart illustrating the mathematical scoring rules leading to the three status badges (SAFE, WARNING, CRITICAL).
- **Speaker Notes:**
  > "A key contribution of our project is the rule-based compliance algorithm implemented in app.py. Rather than treating detection outputs in isolation, our algorithm mathematically correlates the number of detected persons with detected protective gear. It applies an immediate 15% penalty for every explicit negative detection, calculates helmet and vest ratios, and categorizes the work site into one of three operational risk tiers: Safe, Warning, or Critical."

---

### Slide 12: Asynchronous Alerting System
- **Slide Number:** 12
- **Slide Title:** Asynchronous Email Dispatch & Incident Reporting
- **Presentation Content:**
  - **Non-Blocking Architecture:** Email dispatch runs inside a background daemon thread (`threading.Thread`) so user web requests complete in milliseconds.
  - **Rich HTML Reporting:** Dispatches an executive-styled email template containing:
    - Status badge (`CRITICAL` / `WARNING`)
    - Exact timestamp of the event
    - Itemized list of safety violations
    - Object count summary table
  - **Annotated Visual Attachment:** Automatically attaches the output image highlighting violators with colored bounding boxes.
  - **Anti-Flooding Cooldown:** Enforces a configurable 30-second cooldown window to prevent inbox saturation during consecutive detections.
- **Suggested Visual:**
  - Screenshot of the actual HTML email template received in an inbox, showing the red CRITICAL banner, detection table, and attached image.
- **Speaker Notes:**
  > "When a safety violation occurs, timely notification is essential. In alerts.py, we implemented an asynchronous alerting engine. By spawning a separate daemon thread, the web server never freezes while connecting to the mail server. It sends a structured HTML report with exact timestamps and violation lists, and attaches the annotated image as visual proof. Furthermore, a built-in 30-second cooldown timer prevents email flooding during consecutive frames."

---

### Slide 13: Step-by-Step System Workflow
- **Slide Number:** 13
- **Slide Title:** Step-by-Step Operational Workflow
- **Presentation Content:**
  - **Step 1:** Server boots, checks for GPU acceleration (`CUDA:0` vs `CPU`), and pre-loads model weights.
  - **Step 2:** User accesses `http://localhost:5000` and drags an inspection image into the upload dropzone.
  - **Step 3:** Flask validates file security, assigns a UUID, and saves the file to `static/uploads/`.
  - **Step 4:** YOLO executes inference with confidence threshold $\tau = 0.25$ and saves the annotated visual output.
  - **Step 5:** The compliance engine evaluates person-to-gear counts and calculates compliance percentage.
  - **Step 6:** If violations are detected, an email alert is dispatched asynchronously.
  - **Step 7:** The frontend displays original vs. annotated images side-by-side with full analytics.
- **Suggested Visual:**
  - Horizontal timeline graphic with icons representing each of the 7 operational steps from user upload to UI display and email delivery.
- **Speaker Notes:**
  > "Here is the complete user journey from start to finish. The server initializes the model once at startup to eliminate latency. When a user uploads a site photo, the system validates the file, runs YOLO detection, evaluates safety rules, generates annotated images, and triggers background email alerts if necessary—all while updating the dashboard in less than a second."

---

### Slide 14: Model Training Configuration & Results
- **Slide Number:** 14
- **Slide Title:** Experimental Training Results (50 Epochs)
- **Presentation Content:**
  - **Training Environment:** Local GPU execution (Device `0`), batch size 16, image size 640.
  - **Loss Functions:** Box Loss (CIoU), Class Loss (BCE), Distribution Focal Loss (DFL).
  - **Verified Metric Progress Across 50 Epochs:**
    | Training Stage | Train Cls Loss | Precision | Recall | mAP@50 | mAP@50-95 |
    | :--- | :---: | :---: | :---: | :---: | :---: |
    | **Epoch 1** | 4.805 | 0.85% | 20.19% | 3.93% | 2.06% |
    | **Epoch 10** | 1.982 | 63.49% | 39.89% | 41.36% | 20.15% |
    | **Epoch 25** | 1.454 | 69.30% | 46.21% | 47.65% | 24.04% |
    | **Epoch 50 (Final)** | **1.040** | **60.79%** | **51.61%** | **52.30%** | **26.00%** |
  - **Loss Reduction:** Classification loss dropped by **78.4%**, demonstrating robust convergence.
- **Suggested Visual:**
  - Training metrics plot showing the mAP@50 curve ascending from 3.9% to 52.3%, alongside the declining loss curve (`results.png` from `train-4`).
- **Speaker Notes:**
  > "These are the verified experimental results from our 50-epoch training run in train-4. In epoch 1, the model started with an mAP@50 of just 3.9% and a classification loss of 4.80. Over 50 epochs, classification error decreased by 78.4%, converging to an overall precision of 60.8%, recall of 51.6%, and an mAP@50 of 52.3%. These metrics confirm that the model learned meaningful representations for both workers and protective equipment."

---

### Slide 15: Web Dashboard & Detection Showcase
- **Slide Number:** 15
- **Slide Title:** Web Dashboard & Real-World Detection Showcase
- **Presentation Content:**
  - **Glassmorphism Interface:** Designed for clear visibility in site control rooms and supervisor tablets.
  - **Live Hardware Telemetry:** Displays current processing unit (`CUDA:0 (Tesla T4)` or `CPU`).
  - **Comparative Visualizer:** Side-by-side view of the original photo and the AI-annotated output with colored bounding boxes.
  - **Live Metric Gauges:** Displays overall compliance score alongside counts for persons, helmets, and vests.
  - **Alert Banner:** Dynamic top banner flashing red for safety violations or green when full compliance is confirmed.
- **Suggested Visual:**
  - High-resolution screenshot of the PPEGuard web dashboard displaying a test image (e.g., `ppe-inference-im0.png` or `worker.jpeg`) with detected bounding boxes, violation lists, and the compliance score card.
- **Speaker Notes:**
  > "Here is our actual web interface in action. We designed a modern, dark-mode dashboard tailored for safety control rooms. In this test run on an active job site photo, the system detected five workers, but only two helmets and zero vests. The compliance score immediately dropped to 40%, the status banner flashed red for CRITICAL, and an itemized violation list appeared on the right. Simultaneously, an email alert was dispatched to the supervisor."

---

### Slide 16: Advantages & Technical Strengths
- **Slide Number:** 16
- **Slide Title:** Key Advantages & Technical Strengths
- **Presentation Content:**
  - **Full-Stack End-to-End Implementation:** Complete integration from raw PyTorch training to browser-based inference and automated email delivery.
  - **Explainable Safety Logic:** Compliance scores are calculated using clear, interpretable mathematical formulas rather than an opaque black box.
  - **Non-Blocking Architecture:** Threaded email handling guarantees zero HTTP request stalling.
  - **Lightweight & Portable:** At just 2.5 million parameters and 5.39 MB, YOLO26n runs efficiently on edge hardware and standard CPUs.
  - **Dual-Perspective Class Training:** Directly detects negative non-compliance classes (`no_helmet`, `no_vest`) alongside standard equipment.
- **Suggested Visual:**
  - Grid of icons representing: Explainability, Speed, Edge Compatibility, Non-Blocking Concurrency, and Dual-Perspective Detection.
- **Speaker Notes:**
  > "The primary strengths of PPEGuard lie in its integration, explainability, and speed. It provides a complete end-to-end pipeline from model weights to live web UI. Our compliance math is fully interpretable and transparent. Thanks to our multi-threaded design, email alerts never slow down user interactions. Finally, the lightweight nature of YOLO26n makes it suitable for deployment on low-cost edge computers."

---

### Slide 17: Limitations & Operational Challenges
- **Slide Number:** 17
- **Slide Title:** Current Limitations & Engineering Challenges
- **Presentation Content:**
  - **Single-Image Ingestion:** The current web interface processes individual uploaded photos rather than continuous RTSP live video streams.
  - **Class Imbalance in Training Data:** Negative classes like `no_boots` and `no_goggle` have fewer annotated training instances, leading to lower recall for those specific classes.
  - **Small-Object Challenges at Distance:** Detecting small items (like safety goggles or gloves) remains difficult when workers are far from the camera lens.
  - **Stateless Database Architecture:** Inspection results are currently stored as filesystem images and volatile JSON responses rather than in a relational database (SQLite/PostgreSQL).
- **Suggested Visual:**
  - Diagram highlighting challenge scenarios: Camera distance/perspective distortion, small object occlusion, and mail server credential dependencies.
- **Speaker Notes:**
  > "In the spirit of honest scientific inquiry, we must also acknowledge current limitations. PPEGuard currently processes uploaded static photos rather than continuous live video feeds. Small items like goggles are harder to detect at long distances, and negative classes like 'no_boots' had fewer training examples in the dataset. Additionally, our inspection history currently resides in filesystem folders rather than a persistent SQL database."

---

### Slide 18: Future Scope & Roadmap
- **Slide Number:** 18
- **Slide Title:** Future Scope & Technical Roadmap
- **Presentation Content:**
  - **1. Live RTSP / CCTV Integration:** Connect OpenCV/WebRTC to ingest live video feeds from IP cameras at 15–30 FPS.
  - **2. 100-Epoch Cloud Retraining:** Execute our prepared `train_colab.py` script on a Tesla T4 GPU to train for 100 epochs and improve mAP.
  - **3. Historical Database & Audit Analytics:** Integrate PostgreSQL to log every inspection, tracking compliance trends over time.
  - **4. Edge Optimization with TensorRT / ONNX:** Deploy exported ONNX models onto NVIDIA Jetson Orin microcomputers for on-site edge processing.
  - **5. Multi-Channel Alerting:** Extend notifications beyond email to include SMS (Twilio), WhatsApp, and Slack/Teams webhooks.
- **Suggested Visual:**
  - A 4-phase evolutionary roadmap: [Phase 1: Current Image Web App] -> [Phase 2: Live RTSP CCTV Streams] -> [Phase 3: Database & Analytics] -> [Phase 4: Jetson Edge Deployment].
- **Speaker Notes:**
  > "Looking forward, we have established a clear technical roadmap. First, we plan to support live RTSP video streams from existing site cameras. Second, we have already prepared scripts to train for 100 epochs on cloud GPUs to further boost model accuracy. Third, adding database logging will enable longitudinal compliance analytics. Finally, deploying via ONNX or TensorRT onto edge devices like the NVIDIA Jetson will allow on-site, self-contained operation."

---

### Slide 19: Conclusion
- **Slide Number:** 19
- **Slide Title:** Conclusion: Transforming Worksite Safety with AI
- **Presentation Content:**
  - **Summary:** Developed and validated PPEGuard, an automated AI-driven workplace safety monitoring system.
  - **Model Verification:** Successfully fine-tuned YOLO26 Nano on the 1,416-image Construction-PPE dataset, achieving 52.3% mAP@50 and 60.8% precision.
  - **System Integration:** Connected deep learning inference to a mathematical compliance engine, a dark-mode web dashboard, and an automated email alerting pipeline.
  - **Key Takeaway:** Demonstrates that modern deep learning and lightweight computer vision can transition workplace safety from passive recording to active, automated incident prevention.
- **Suggested Visual:**
  - High-impact closing visual combining the PPEGuard logo, the annotated output image, and a green "Safety Verified" seal.
- **Speaker Notes:**
  > "In conclusion, PPEGuard demonstrates how modern computer vision can transform workplace safety. By combining a fine-tuned YOLO26 Nano model with an explainable compliance algorithm and automated alerting, we built a functional, end-to-end system that can actively prevent workplace accidents. We have met all project objectives, and the codebase provides a strong foundation for future live-stream and edge deployments. Thank you, and we welcome your questions."

---

### Slide 20: References & Citations
- **Slide Number:** 20
- **Slide Title:** Key References & Acknowledgments
- **Presentation Content:**
  1. **Ultralytics YOLO Documentation & Models:**  
     *YOLOv8 / YOLO11 / YOLO26 Architecture & Models*, Ultralytics Inc., 2024–2026. `https://docs.ultralytics.com`
  2. **Construction-PPE Dataset:**  
     *Construction PPE Detection Benchmark Dataset*, Ultralytics Hub, AGPL-3.0 License. `https://docs.ultralytics.com/datasets/detect/construction-ppe/`
  3. **PyTorch Framework:**  
     Paszke, A., et al., *PyTorch: An Imperative Style, High-Performance Deep Learning Library*, NeurIPS.
  4. **Flask Web Framework:**  
     Pallets Projects, *Flask WSGI Framework Documentation (v3.x)*, `https://flask.palletsprojects.com/`
  5. **Safety Standards & Regulations:**  
     Occupational Safety and Health Administration (OSHA), *Standard 29 CFR 1926.95 / 1926.100 - Personal Protective Equipment*.
- **Suggested Visual:**
  - Clean academic bibliography layout with an institutional logo and "Thank You / Q&A" contact footer.
- **Speaker Notes:**
  > "These are the primary academic, technical, and regulatory references that guided our research and implementation. We thank our project guide and department faculty for their support throughout this work. We are now open for questions."
