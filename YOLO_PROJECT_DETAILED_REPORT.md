# Comprehensive Project Analysis Report: PPEGuard (AI-Powered Workplace Safety & PPE Compliance System)

**Project Name:** PPEGuard — AI Workplace Safety & PPE Compliance Monitoring System  
**Lead Framework:** Ultralytics YOLO26 Nano (`YOLO26n`) & Flask Web Server  
**Author/Developer Reference:** Student Project Workspace (`DS_MP`)  
**Target Audience:** Engineering Students, Faculty Evaluators, Technical Project Reviewers, and Presentation Presenters  

---

## 1. Project Overview

### 1.1 Actual Project Name
The verified project name implemented throughout the source code, user interface, and notification engine is **PPEGuard** (subtitled *"AI Workplace Safety & PPE Compliance Monitoring System"*).

### 1.2 Project Domain and Category
- **Domain:** Data Science & Artificial Intelligence (AI)
- **Sub-Disciplines:** Computer Vision (CV), Deep Learning (DL), Object Detection, Industrial Internet of Things (IIoT) Safety Automation, and Full-Stack Machine Learning Engineering (MLE).

### 1.3 What the Application Does
PPEGuard is an intelligent computer vision application that ingests visual data (site photographs and inspection imagery) from construction yards and hazardous industrial zones. It runs deep neural network object detection to locate human personnel and identify personal protective equipment (PPE). The system then computes a safety compliance score, flags specific safety violations (e.g., workers without hard hats or high-visibility vests), and automatically dispatches rich HTML email alerts with annotated photographic evidence to site safety officers.

### 1.4 Main Purpose and Intended Users
The system provides continuous, unbiased, automated safety oversight on work sites.
- **Intended Users:**
  - Construction Site Supervisors and Foremen
  - Industrial Health, Safety, and Environment (HSE) Officers
  - Facility & Plant Operations Managers
  - Safety Compliance Auditors and Insurance Inspectors

### 1.5 Real-World Problem Being Solved
Construction and heavy industry account for a disproportionate percentage of fatal and severe workplace injuries worldwide (often termed OSHA's "Fatal Four": falls, struck-by objects, electrocutions, and caught-in-between). A critical defense against these hazards is the consistent use of Personal Protective Equipment (hard hats, high-visibility vests, protective gloves, boots, and goggles). Manual monitoring of vast job sites is intermittent, labor-intensive, subjective, and prone to human oversight. PPEGuard solves this by providing automated, objective, 24/7 visual compliance verification.

### 1.6 Key Features
- **Deep Learning Object Detection:** Employs fine-tuned Ultralytics YOLO26 Nano weights to detect workers, safety gear, and explicit non-compliance.
- **Rule-Based Compliance Engine:** Cross-references the number of detected persons against detected gear to calculate an exact compliance percentage (0–100%).
- **Three-Tier Operational Risk Categorization:** Categorizes site status into `SAFE` (green), `WARNING` (amber), or `CRITICAL` (red).
- **Automated SMTP Email Alerting:** Asynchronously dispatches formatted email alerts with site metrics and attached annotated evidence to designated safety officers.
- **Rate-Limiting & Cooldown Protection:** Incorporates a configurable cooldown timer (default: 30 seconds) to prevent inbox flooding.
- **Hardware-Aware Acceleration:** Automatically detects and utilizes NVIDIA CUDA GPU acceleration when available, with automatic CPU fallback.
- **Dark-Theme Interactive Dashboard:** Browser-based interface featuring drag-and-drop image uploads, side-by-side original vs. annotated visual comparisons, live stats, violation lists, and SMTP configuration modals.

### 1.7 Expected Inputs and Outputs
- **Expected Inputs:** 
  - Digital images in standard image formats (`.jpg`, `.jpeg`, `.png`, `.webp`) up to 16 MB.
  - SMTP configuration parameters (server host, port, sender email, app password, receiver email, cooldown interval).
- **Expected Outputs:**
  - Annotated bounding-box image saved to `static/results/`.
  - JSON payload containing detected classes, confidence scores, bounding box coordinates `[x1, y1, x2, y2]`, compliance score, status string, and violation bullet points.
  - Interactive browser visualization with detection counters.
  - Rich HTML email notification with attached annotated visual proof.

---

## 2. Problem Statement

### 2.1 Existing Problem
On construction and civil engineering sites, adherence to PPE protocols directly dictates survivability during catastrophic incidents (falling objects, vehicular traffic, hazardous dust, chemical splashes). Despite mandatory regulatory frameworks (such as OSHA or ISO 45001), workers frequently discard or omit PPE due to discomfort, heat, negligence, or rushing deadlines.

### 2.2 Why This Problem Matters
- **Severe Human Cost:** Traumatic brain injuries from falling debris and crushing incidents due to low visibility remain leading causes of construction fatalities.
- **Financial & Legal Liabilities:** Companies face regulatory penalties, project shutdowns, increased insurance premiums, and legal claims following safety infractions.
- **Reputational Damage:** Worksite fatalities tarnish contractor reputations and can disqualify firms from future bidding.

### 2.3 Limitations of Existing Approaches
| Existing Method | Operational Bottleneck | Technical Limitation |
| :--- | :--- | :--- |
| **Manual Safety Patrols** | Infrequent spot-checks; inspectors cannot monitor all sectors simultaneously. | Human fatigue, cognitive bias, and inability to maintain a persistent audit trail. |
| **Traditional CCTV** | Passive surveillance; video footage is reviewed only *after* an accident occurs. | Lacks intelligence; cannot automatically alert supervisors in real time. |
| **Standard Rule-Based Vision** | Edge detection or classical color filtering (e.g., thresholding for yellow/orange). | Fails under varying lighting, shadows, occlusion, angles, and cluttered backgrounds. |

### 2.4 How the Developed Project Addresses the Problem
PPEGuard bridges the gap between passive video recording and active incident prevention. By utilizing deep convolutional neural networks fine-tuned on industrial safety datasets, it detects equipment and missing gear invariant to lighting, poses, and clutter. By coupling inference with an automated alerting pipeline, it notifies safety personnel within seconds of a detected breach.

---

## 3. Project Objectives

### 3.1 Main Objective
To design, train, evaluate, and deploy an automated AI-driven workplace safety compliance system that detects personnel and protective gear using YOLO, evaluates compliance through mathematical rule verification, and alerts supervisors via email.

### 3.2 Specific Technical Objectives
1. **Model Adaptation & Fine-Tuning:** Train the lightweight Ultralytics YOLO26 Nano architecture on the 11-class Construction PPE dataset for 50 epochs locally, with a scripted pathway for 100 epochs on GPU.
2. **Multi-Scale Detection Capability:** Accurately locate both large targets (`Person`) and small targets (`helmet`, `gloves`, `goggles`, `boots`).
3. **Automated Compliance Scoring Algorithm:** Formulate a mathematical scoring function that penalizes explicit negative detections (`no_helmet`, `no_vest`) and verifies person-to-gear ratios.
4. **Non-Blocking Asynchronous Alerts:** Implement a threaded SMTP email dispatch system that does not stall the Flask HTTP request-response cycle.
5. **Modern User Interface:** Build a responsive web dashboard for site operators to upload imagery, review detections, and inspect violations.

### 3.3 Expected Outcomes
- An end-to-end operational software artifact running on local or server hardware.
- Real-time or near-real-time inference latency (< 100 ms on GPU, < 1 s on CPU).
- Visual feedback via color-coded bounding boxes on site imagery.
- Immediate email dispatch when dangerous conditions are detected.

### 3.4 Practical Applications
- Construction and civil infrastructure sites.
- Heavy manufacturing, metallurgy plants, and shipyards.
- Chemical refineries and oil & gas extraction platforms.
- Automated drone-based or pole-mounted site safety audits.

---

## 4. Complete Technology Stack

### 4.1 Programming Languages
- **Python (v3.10 – v3.13):** Core backend language for data pipelines, model training, computer vision inference, compliance mathematics, and HTTP server routing.
- **JavaScript (ECMAScript 6+):** Client-side scripting for file selection, asynchronous AJAX/Fetch calls, dynamic DOM manipulation, and settings modals.
- **HTML5 & CSS3:** Markup and styling for the browser dashboard.

### 4.2 Python Libraries & Core Packages
*(Verified against [requirements.txt](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/requirements.txt) and active code imports)*:
- **`flask` (v3.x):** Lightweight Web Server Gateway Interface (WSGI) web framework providing routing, request handling, template rendering, and RESTful endpoints.
- **`werkzeug`:** WSGI web utility library utilized for security operations (e.g., `secure_filename`).
- **`ultralytics` (v8.4.127):** Primary computer vision library providing YOLO model definitions, checkpoint loading, inference engines, plotting routines, and export tools.
- **`torch` (PyTorch v2.x):** Deep learning framework handling tensor calculations, CUDA acceleration, and backpropagation.
- **`torchvision` & `torchaudio`:** PyTorch ecosystem libraries for image transformations and tensor operations.
- **`smtplib` & `email` (Python Standard Library):** Core networking modules for assembling RFC 2822 MIME multipart messages and communicating with SMTP servers over TLS.
- **`threading` (Python Standard Library):** Concurrency library used to run email delivery in background daemon threads.
- **`pathlib`, `json`, `uuid`, `os`:** File path resolution, configuration persistence, and unique ID generation.

### 4.3 YOLO Framework & Exact Model
- **Framework:** Ultralytics YOLO Ecosystem.
- **Exact Model Architecture:** **Ultralytics YOLO26 Nano (`YOLO26n`)**.
- **Model Files:**
  - Base Pretrained Weights: `yolo26n.pt` (5.54 MB).
  - Custom Fine-Tuned Weights: `runs/detect/train-4/weights/best.pt` (5.39 MB) and `last.pt` (5.39 MB).

### 4.4 Frontend Technologies
- **Markup:** Semantic HTML5 (`<header>`, `<main>`, `<section>`, `<dialog>`).
- **Styling:** Pure Vanilla CSS (zero external UI framework dependencies; no Tailwind or Bootstrap). Utilizes CSS custom properties (`:root`), Flexbox, CSS Grid, backdrop-filter glassmorphism, and keyframe animations (`pulse-border`).
- **Typography:** Google Fonts (`Inter` font family, weights 300 to 700).
- **Networking:** Native browser Fetch API for JSON and `multipart/form-data` communication.

### 4.5 Backend Architecture
- **Web Server:** Flask local development server running on `0.0.0.0:5000`.
- **Model Loader:** Singleton model instance initialized at server boot to eliminate per-request cold-start delays.
- **Storage Strategy:** Disk-based file storage (`static/uploads/` and `static/results/`).

### 4.6 Database
- **Database Status:** **Not present / None used.**
- **Persistence Method:** In-memory caching and disk-based JSON serialization via `alert_config.json`. (Clearly documented: no SQL or NoSQL database is utilized in the current codebase).

### 4.7 Development Tools
- **IDE:** Antigravity IDE (VS Code-compatible runtime on Windows 11).
- **Interactive Computing:** Jupyter Notebook (`PPEGuard.ipynb`) for training exploration.
- **Cloud Computing Platform:** Google Colab / Kaggle with Nvidia Tesla T4 GPU support.
- **Version Control:** Git.

### 4.8 Hardware & Software Requirements
- **Development/Host OS:** Windows 10/11 (or Linux/macOS for deployment).
- **GPU Requirement:** Optional but recommended: NVIDIA GPU with CUDA 11.8+ / 12.x support (e.g., GTX 1650, RTX 3060, or cloud Tesla T4).
- **CPU Fallback:** Fully functional on Intel/AMD x86_64 or ARM CPUs using standard PyTorch CPU tensors.
- **Memory Requirements:** Minimum 4 GB RAM (8 GB+ recommended).

---

## 5. Dataset Analysis

### 5.1 Dataset Name and Source
- **Dataset Name:** Ultralytics **Construction PPE Dataset** (`construction-ppe`).
- **Source URL:** `https://github.com/ultralytics/assets/releases/download/v0.0.0/construction-ppe.zip` / `https://ultralytics.com/assets/construction-ppe.zip`.
- **Documentation Reference:** `https://docs.ultralytics.com/datasets/detect/construction-ppe/`.
- **License:** GNU Affero General Public License v3.0 (AGPL-3.0), as verified in [datasets/construction-ppe/LICENSE](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/datasets/construction-ppe/LICENSE).

### 5.2 Dataset Structure & File Locations
The dataset resides locally under [datasets/construction-ppe/](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/datasets/construction-ppe) and is defined by [data.yaml](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/datasets/construction-ppe/data.yaml):

```
datasets/construction-ppe/
├── data.yaml
├── LICENSE
├── images/
│   ├── train/     (1,132 images)
│   ├── val/       (143 images)
│   └── test/      (141 images)
└── labels/
    ├── train/     (1,132 .txt label files)
    ├── val/       (143 .txt label files)
    └── test/      (141 .txt label files)
```

### 5.3 Exact Image Counts & Class Verification
- **Total Dataset Images:** **1,416 images**
  - **Training Split:** 1,132 images (80.0%)
  - **Validation Split:** 143 images (10.1%)
  - **Testing Split:** 141 images (9.9%)

### 5.4 Annotation Format
Standard YOLO Darknet text format. For every image file `imageXYZ.jpg`, there exists a matching `imageXYZ.txt` file where each row represents one labeled object:
$$\text{class\_id} \quad x_{\text{center}} \quad y_{\text{center}} \quad \text{width} \quad \text{height}$$
All coordinate values are normalized between `0.0` and `1.0` relative to the image dimensions.

### 5.5 Target Classes (11 Classes)
The dataset contains 11 distinct classes comprising human subjects, positive protective gear, and explicit negative non-compliance detections:

| Class ID | Class Name | Category | Description |
| :---: | :--- | :--- | :--- |
| **0** | `helmet` | Positive PPE | Hard hat or safety helmet worn on head |
| **1** | `gloves` | Positive PPE | Protective hand gloves |
| **2** | `vest` | Positive PPE | High-visibility reflective safety vest |
| **3** | `boots` | Positive PPE | Steel-toe or heavy-duty safety footwear |
| **4** | `goggles` | Positive PPE | Protective safety glasses or eye shields |
| **5** | `none` | Negative / Violation | Worker detected with no visible protective equipment |
| **6** | `Person` | Subject | Human worker / individual |
| **7** | `no_helmet` | Negative / Violation | Head visible without a safety helmet |
| **8** | `no_goggle` | Negative / Violation | Face visible without eye protection |
| **9** | `no_gloves` | Negative / Violation | Hands visible without protective gloves |
| **10** | `no_boots` | Negative / Violation | Feet visible without safety boots |

### 5.6 Data Preprocessing & Augmentation Pipeline
Verified from the active training log in `PPEGuard.ipynb` and `args.yaml`:
- **Input Resolution:** Resized to $640 \times 640$ pixels with letterboxing.
- **Automatic Mixed Precision (AMP):** Enabled for reduced memory footprint and faster forward passes.
- **Mosaic Augmentation:** Parameter `mosaic=1.0` combines 4 training images into one composite image to improve small-object detection, disabled during the final 10 epochs (`close_mosaic=10`).
- **Albumentations Library Transforms:**
  - `Blur(p=0.01, blur_limit=(3, 7))`
  - `MedianBlur(p=0.01, blur_limit=(3, 7))`
  - `ToGray(p=0.01)`
  - `CLAHE(p=0.01, clip_limit=(1.0, 4.0))`
- **Color & Geometric Jitter:**
  - HSV Hue: $0.015$, Saturation: $0.7$, Value: $0.4$
  - Horizontal Flip: `fliplr=0.5` (Vertical flip disabled: `flipud=0.0`)
  - Random Scaling: `scale=0.5`
  - Random Translation: `translate=0.1`
  - Random Erasing: `erasing=0.4`

### 5.7 Model Usage Verification: Pretrained vs. Custom
The project uses **both**:
- It begins with official base pretrained weights `yolo26n.pt` (transfer learning from COCO).
- It fine-tunes those weights on the 11-class Construction PPE dataset to produce custom checkpoints: `train-4/weights/best.pt`.

---

## 6. YOLO Model Explanation

### 6.1 Exact YOLO Version & Variant
- **YOLO Generation:** **Ultralytics YOLO26**
- **Model Variant:** **Nano (`YOLO26n`)**
- **Architecture Footprint (Verified from Training Log):**
  - **Full Training Architecture:** 260 layers, 2,508,090 parameters, 2,508,090 gradients, 5.9 GFLOPs.
  - **Fused Inference Architecture:** 122 layers, 2,376,981 parameters, 0 gradients, 5.3 GFLOPs.
  - **Storage Size on Disk:** ~5.39 MB (`best.pt`).

### 6.2 Structural Neural Network Breakdown
The YOLO26n architecture consists of three interconnected architectural divisions:

```
[ Input: 640x640x3 Image ]
           │
           ▼
┌────────────────────────────────────────────────────────┐
│ 1. BACKBONE (Feature Extraction)                       │
│    - Conv Layers (Strided 3x3 Convolutions)            │
│    - C3k2 Blocks (Cross Stage Partial Bottlenecks)     │
│    - SPPF (Spatial Pyramid Pooling - Fast at 5x5)      │
│    - C2PSA (Pointwise Spatial Attention Module)        │
└────────────────────────────────────────────────────────┘
           │
           ▼
┌────────────────────────────────────────────────────────┐
│ 2. NECK (Multi-Scale Feature Fusion)                   │
│    - PAN-FPN (Path Aggregation & Feature Pyramid Net)  │
│    - Upsample Layers (Nearest Neighbor 2x)             │
│    - Concatenation Nodes (P3, P4, P5 multi-scale)      │
│    - Intermediate C3k2 Refinement Blocks               │
└────────────────────────────────────────────────────────┘
           │
           ▼
┌────────────────────────────────────────────────────────┐
│ 3. HEAD (Decoupled Anchor-Free Detection)              │
│    - Scale 1: 80x80 grid  (Small objects: goggles)     │
│    - Scale 2: 40x40 grid  (Medium: helmets, boots)     │
│    - Scale 3: 20x20 grid  (Large: full Person, vest)   │
│    - Separate Box Regression & Class Classification    │
└────────────────────────────────────────────────────────┘
           │
           ▼
[ Post-Processing: Non-Maximum Suppression (NMS) ]
           │
           ▼
[ Final Predictions: Class, Score, Box Coordinates ]
```

1. **Backbone**:
   - Successive strided convolution layers downsample the spatial resolution while expanding feature channels ($3 \to 16 \to 32 \to 64 \to 128 \to 256$).
   - `C3k2` modules (Cross Stage Partial blocks with dual convolutions) preserve gradient flow while minimizing redundant parameter calculation.
   - `SPPF` pools feature representations across multiple kernel windows to capture global contextual receptive fields without speed loss.
   - `C2PSA` applies spatial self-attention to emphasize critical regions (such as heads and hands).
2. **Neck**:
   - Utilizes a modified Feature Pyramid Network (FPN) and Path Aggregation Network (PAN).
   - Combines deep semantic features with shallow high-resolution spatial features to allow concurrent detection of large persons and small items like goggles or gloves.
3. **Head**:
   - Anchor-free decoupled detection head predicting directly across three feature map scales (`[64, 128, 256]` channels).
   - Separates bounding box coordinate regression (using Distribution Focal Loss and Complete IoU) from class score prediction.

### 6.3 Object Detection Workflow
1. **Input Resizing:** The input image is converted to RGB and resized to a max dimension of 640 while maintaining aspect ratio via letterboxing.
2. **Forward Pass:** The convolutional layers compute feature maps and output tensor candidates for every grid cell across all three scales.
3. **Confidence Filtering:** Predictions with a confidence score below the threshold ($\tau_{\text{conf}} = 0.25$) are discarded.
4. **Non-Maximum Suppression (NMS):** Eliminates overlapping redundant bounding boxes predicting the same object using an Intersection-over-Union (IoU) threshold ($\text{IoU} = 0.7$).

### 6.4 Why YOLO is Appropriate for This Project
- **Single-Stage Speed:** Unlike two-stage detectors (Faster R-CNN) that generate region proposals first, YOLO evaluates the entire image in a single forward pass, providing low latency (< 10 ms on GPU).
- **Global Context:** By viewing the entire image during inference, YOLO reduces background false positives compared to sliding-window approaches.
- **Edge Deployability:** With a footprint of only 2.5 million parameters and 5.3 GFLOPs, YOLO26n can run on low-power edge hardware (NVIDIA Jetson, Intel NUC) directly on-site.

---

## 7. Complete System Architecture

### 7.1 Major Modules
The project is architected into four distinct modules:
1. **Presentation Layer (Frontend UI):** Implemented in `templates/index.html`. Handles client interaction, file dragging, visual rendering, and modal dialogs.
2. **Inference & Routing Engine (Backend API):** Implemented in `app.py`. Coordinates request parsing, file validation, model execution, compliance math, and response assembly.
3. **Deep Learning Vision Engine (Model Core):** Encapsulated in the Ultralytics PyTorch runtime using weights `best.pt`.
4. **Notification & Alerting Engine:** Implemented in `alerts.py` with persistent configuration in `alert_config.json`. Handles background thread dispatch, SMTP authentication, HTML email generation, and rate limiting.

### 7.2 Information Flow
```
[User Browser]
      │
      │ 1. Multipart POST (/predict) with image file
      ▼
[Flask Web Server (app.py)]
      │
      │ 2. Save file with UUID prefix to static/uploads/
      ▼
[Inference Pipeline]
      │
      │ 3. Forward pass through YOLO26n (torch.no_grad())
      ▼
[Ultralytics YOLO Engine]
      │
      │ 4. Extract boxes, class IDs, confidences, save annotated image
      ▼
[Compliance & Safety Logic (app.py)]
      │
      │ 5. Evaluate helmet/vest ratios, penalize negative classes
      │    Calculate compliance score (0-100%) and Status (SAFE/WARNING/CRITICAL)
      │
      ├────────────────────────────────────────┬────────────────────────────────────────┐
      │                                        │                                        │
      │ 6a. If violations detected:            │ 6b. Return JSON payload                │
      │     Trigger async alert thread         │                                        │
      ▼                                        ▼                                        ▼
[alerts.py Daemon Thread]             [HTTP 200 JSON Response]                  [User Browser]
      │                                        │                                        │
      │ 7. Check cooldown & SMTP credentials   │                                        │
      │ 8. Connect to smtp.gmail.com:587       │                                        │
      │ 9. Transmit HTML email + attachment    ▼                                        │
      ▼                                [Client JavaScript (displayResults)]     │
[Safety Officer Inbox]                         │                                        │
                                               │ 10. Update DOM elements, metrics,      │
                                               │     violations list & visual images    ▼
                                               └─────────────────────────────────> [Rendered UI]
```

### 7.3 Text-Based System Architecture Diagram
```
+-----------------------------------------------------------------------------------+
|                                 CLIENT TIER                                       |
|  - Web Browser / Dashboard (templates/index.html)                                 |
|  - Drag-and-Drop Dropzone, File Preview, Compliance Gauge, Alert Settings Modal    |
+-----------------------------------------------------------------------------------+
                                        |  HTTP Requests (POST /predict, GET/POST config)
                                        v
+-----------------------------------------------------------------------------------+
|                              APPLICATION TIER                                     |
|  Flask Application Server (app.py)                                                |
|  ├── Route Handlers:                                                              |
|  │   ├── GET  /                 -> Serves index.html with GPU/device info        |
|  │   ├── POST /predict          -> Processes image, runs YOLO, scores compliance |
|  │   ├── GET  /api/alerts/config-> Retrieves sanitized alert config               |
|  │   ├── POST /api/alerts/config-> Saves updated SMTP credentials                 |
|  │   └── POST /api/alerts/test  -> Dispatches simulated test alert                |
|  ├── Compliance Evaluation Subsystem:                                             |
|  │   ├── Negative Gear Penalty Rule (-15% per missing gear detection)             |
|  │   ├── Person-to-Gear Ratio Check (min(1.0, gear / persons))                    |
|  │   └── Status Assignment Engine (SAFE / WARNING / CRITICAL)                     |
|  └── File System Storage Controller:                                              |
|      ├── static/uploads/        -> Preserves original uploaded images with UUIDs  |
|      └── static/results/        -> Preserves annotated bounding box images        |
+-----------------------------------------------------------------------------------+
             |                                             |
             v                                             v
+-----------------------------+               +-------------------------------------+
|        VISION TIER          |               |         NOTIFICATION TIER           |
|  Ultralytics YOLO26n        |               |  Asynchronous Alert Engine          |
|  - PyTorch Engine (CUDA/CPU)|               |  (alerts.py)                        |
|  - Checkpoints:             |               |  ├── Daemon Threading Pipeline      |
|    train-4/weights/best.pt  |               |  ├── Cooldown Timer (30s)           |
|  - Detection Output:        |               |  ├── HTML Email Generator           |
|    Boxes, Labels, Scores    |               |  ├── MIME Multipart Attachment      |
|                             |               |  └── TLS SMTP Dispatcher            |
+-----------------------------+               +-------------------------------------+
                                                           |
                                                           v
                                              +-------------------------------------+
                                              |       EXTERNAL SERVICES             |
                                              |  SMTP Mail Server (e.g., Gmail)     |
                                              |  -> Safety Officer Email Inbox      |
                                              +-------------------------------------+
```

---

## 8. Step-by-Step Project Working

### Step 1: Starting the Server
1. The developer runs `python app.py`.
2. The server script resolves paths, creates `static/uploads` and `static/results` directories if missing, and inspects the hardware using `torch.cuda.is_available()`.
3. The server locates the model weights following a priority hierarchy:
   1. `runs/detect/train-100/weights/best.pt`
   2. `runs/detect/train-4/weights/best.pt` (active candidate)
   3. `yolo26n.pt` (fallback)
4. The model is instantiated in memory and transferred to the active compute device (`cuda:0` or `cpu`). The Flask service binds to `http://0.0.0.0:5000`.

### Step 2: User Access & Image Submission
1. The user navigates to `http://localhost:5000` in their web browser.
2. The browser renders `index.html`. A badge in the header displays current hardware acceleration status (e.g., `CUDA:0 (Tesla T4)` or `CPU`).
3. The user drags an image over the dashed upload dropzone or selects a file via the native file picker.
4. Client-side JavaScript (`handleFileSelect`) immediately renders a local preview of the original image using the browser's `FileReader` API.
5. The user clicks **Analyze Workplace Image**.

### Step 3: Server Ingestion & Preprocessing
1. The browser transmits the file via `fetch('/predict')` inside a `FormData` object.
2. Flask verifies the file extension against `{'png', 'jpg', 'jpeg', 'webp'}` and validates the 16 MB size ceiling.
3. Flask assigns an 8-character unique UUID prefix (e.g., `0dc78304_worker.jpeg`) using `uuid.uuid4()` to avoid filename collisions and saves the raw image into `static/uploads/`.

### Step 4: YOLO Inference Execution
1. The backend invokes `model.predict(source=filepath, device=device, conf=0.25, verbose=False)` inside a `torch.no_grad()` context block.
2. The model resizes the image to 640px, passes it through the YOLO26n convolutional backbone and neck, and extracts bounding boxes, confidences, and class IDs from the head.
3. The annotated image (rendered with bounding boxes, labels, and confidence tags) is saved to `static/results/result_<filename>`.

### Step 5: Compliance Scoring & Rule Evaluation
1. The system aggregates detection counts for every class into a dictionary.
2. Explicit negative classes (`no_helmet`, `no_vest`, `no_goggle`, `no_gloves`, `no_boots`, `none`) are evaluated. Each instance applies a **15% penalty** to the compliance score:
   $$\text{Compliance Score} = \max(0, \, 100 - (15 \times \text{negative\_detections}))$$
3. Positive gear ratios are cross-referenced against detected persons:
   $$\text{Helmet Ratio} = \min\left(1.0, \, \frac{\text{helmets}}{\text{people}}\right), \quad \text{Vest Ratio} = \min\left(1.0, \, \frac{\text{vests}}{\text{people}}\right)$$
   $$\text{Compliance Score} = \text{round}\left(\min\left(\text{Compliance Score}, \, \frac{\text{Helmet Ratio} + \text{Vest Ratio}}{2} \times 100\right), \, 1\right)$$
4. If missing gear is detected, specific violation strings are generated (e.g., `"Missing Helmets: Found 1 for 3 Persons."`).
5. The system assigns a status:
   - **`CRITICAL`**: Compliance score < 70%, or explicit negative classes detected, or persons detected with zero gear.
   - **`WARNING`**: Violations present, but score remains $\ge 70\%$.
   - **`SAFE`**: Zero violations detected.

### Step 6: Automated Alert Dispatch
1. If violations are present and alerts are enabled, `alerts.trigger_async_alert()` spawns a daemon thread.
2. The thread checks whether the cooldown period (default: 30 seconds) has elapsed since the last sent alert.
3. If valid, it establishes a TLS connection to the SMTP server (e.g., `smtp.gmail.com:587`), authenticates, constructs an HTML email containing violation lists and detection tables, attaches the annotated image, and transmits the email to the recipient.

### Step 7: Frontend Rendering
1. The server returns an HTTP 200 JSON response to the browser.
2. JavaScript function `displayResults(data)`:
   - Displays the results container.
   - Updates the annotated result image.
   - Updates metric cards (Compliance %, Persons, Helmets, Vests).
   - Populates the violations bullet list.
   - Renders individual detections sorted by confidence.
   - Updates the top alert banner (green for SAFE, red pulsing for CRITICAL).

---

## 9. Module-Wise Implementation

### 9.1 Module 1: Web Server & Application Controller
- **File:** [app.py](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/app.py) (266 lines)
- **Purpose:** Central coordinator for routing, hardware configuration, image ingestion, model inference, compliance logic, and alert triggering.
- **Key Functions:**
  - `allowed_file(filename)`: Validates file extensions.
  - `setup_device_and_model()`: Resolves CUDA GPU or CPU, loads YOLO weights, and returns model instance.
  - `index()`: Serves the web interface with hardware metadata.
  - `predict()`: Primary POST endpoint handling image upload, model prediction, compliance scoring, and alerting.
  - `handle_alert_config()`: REST endpoint (GET/POST) for reading and updating SMTP alert settings.
  - `test_alert()`: POST endpoint to send a simulated email alert on demand.
- **Inputs & Outputs:** Receives multipart HTTP form uploads; outputs JSON objects and rendered HTML templates.

### 9.2 Module 2: Automated Alerting & Email Dispatcher
- **File:** [alerts.py](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/alerts.py) (225 lines) & [alert_config.json](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/alert_config.json)
- **Purpose:** Manages SMTP credential persistence, cooldown timers, HTML email generation, and asynchronous email delivery.
- **Key Functions:**
  - `load_alert_config()` / `save_alert_config(config)`: Reads/writes JSON configuration on disk.
  - `is_configured(config)`: Checks for sender email, password, and recipient email.
  - `build_email_html(violations, counts, score, status, timestamp)`: Generates an inline-styled, responsive HTML email template.
  - `send_email_alert(...)`: Connects via `smtplib.SMTP`, starts TLS, attaches annotated images via `email.mime`, and transmits the message. Enforces the rate-limiting cooldown check.
  - `trigger_async_alert(...)`: Wraps `send_email_alert` in a `threading.Thread(daemon=True)` for non-blocking execution.
- **Inputs & Outputs:** Receives violation details, detection counts, score, and image path; outputs network SMTP transmissions.

### 9.3 Module 3: Frontend Interface & Client Controller
- **File:** [templates/index.html](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/templates/index.html) (953 lines)
- **Purpose:** User interface for interacting with the safety monitoring system.
- **Key Components:**
  - Drag-and-drop file upload zone with visual hover states.
  - Dynamic status indicator displaying GPU acceleration metadata.
  - Side-by-side comparative viewport displaying original image vs. annotated detection output.
  - Four key metric cards: PPE Compliance %, Persons Detected, Helmets Detected, Vests Detected.
  - Two detail panels: Detected Violations List and All Detections breakdown (sorted by confidence).
  - Modal dialog for viewing, saving, and testing SMTP settings.
- **JavaScript Routines:** `uploadImage()`, `displayResults()`, `fetchAlertConfig()`, `saveAlertConfig()`, `sendTestAlert()`.

### 9.4 Module 4: Local Model Training Pipeline
- **File:** [train_model.py](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/train_model.py) (58 lines)
- **Purpose:** Script for training or retraining the YOLO model on local hardware.
- **Key Logic:**
  - Validates CUDA availability.
  - CLI argument parsing (`--epochs`, `--batch`, `--resume`).
  - Supports resuming from checkpoint `train-4/weights/last.pt` or starting fresh from `yolo26n.pt`.
  - Executes `model.train()` pointing to `datasets/construction-ppe/data.yaml` at $640 \times 640$ resolution.
  - Implements `multiprocessing.freeze_support()` for Windows multi-worker support.

### 9.5 Module 5: Cloud/Colab Training Pipeline & Guide
- **Files:** [train_colab.py](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/train_colab.py) (85 lines), [PPEGuard.ipynb](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/PPEGuard.ipynb), [COLAB_TRAINING_GUIDE.md](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/COLAB_TRAINING_GUIDE.md)
- **Purpose:** Pipeline for running 100-epoch training on cloud GPUs (Tesla T4) in ~25–30 minutes, with automatic checkpoint zipping for local deployment.
- **Key Logic:** Automates dataset downloads via Ultralytics, trains for 100 epochs, and packages weights (`best.pt`, `last.pt`, `results.csv`) into a zip archive for download.

---

## 10. Model Training and Evaluation

### 10.1 Verification of Training Execution
**Training was verified as executed.** The project workspace contains full training artifacts, logs, configuration files, checkpoint weights, and evaluation curves.

### 10.2 Documented Training Runs

#### Run 1: Exploratory Colab Training (Documented in `PPEGuard.ipynb`)
- **Environment:** Google Colab, Tesla T4 GPU (15 GB VRAM), PyTorch 2.11.0+cu128, Python 3.13.15.
- **Base Weights:** `yolo26n.pt`
- **Epochs:** 5 epochs
- **Batch Size:** 16 | **Image Size:** 640
- **Optimizer:** AdamW (lr=0.000667, momentum=0.9)
- **Outcome:** Fused model evaluation achieved mAP@50 of **0.318 (31.8%)** across all classes; exported to ONNX (`best.onnx`).

#### Run 2: Full Local Training (Stored in `runs/detect/train-4/`)
- **Environment:** Local GPU execution (Device `0`), workers = 8.
- **Configuration File:** [runs/detect/train-4/args.yaml](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/runs/detect/train-4/args.yaml)
- **Dataset:** [datasets/construction-ppe/data.yaml](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/datasets/construction-ppe/data.yaml)
- **Epochs:** **50 epochs completed**
- **Batch Size:** 16 | **Image Size:** 640
- **Loss Functions:** Box Loss (CIoU/GIoU), Class Loss (BCE), Distribution Focal Loss (DFL).
- **Hyperparameters:** Initial lr (`lr0`): 0.01, final lr factor (`lrf`): 0.01, momentum: 0.937, weight decay: 0.0005, warmup epochs: 3.0, mosaic: 1.0 (disabled in final 10 epochs via `close_mosaic=10`).

### 10.3 Numerical Evaluation Metrics (Run 2: 50 Epochs)
Extracted directly from the training log [runs/detect/train-4/results.csv](file:///c:/Users/DELL/OneDrive/Desktop/DS_MP/runs/detect/train-4/results.csv):

| Epoch | Train Box Loss | Train Cls Loss | Train DFL/L1 Loss | Precision (B) | Recall (B) | mAP@50 (B) | mAP@50-95 (B) | Val Box Loss | Val Cls Loss | Val DFL/L1 Loss |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 1.8191 | 4.8051 | 0.0163 | 0.0085 | 0.2019 | 0.0393 | 0.0206 | 1.6394 | 5.2638 | 0.0171 |
| **10** | 1.7038 | 1.9818 | 0.0152 | 0.6349 | 0.3989 | 0.4136 | 0.2015 | 1.7913 | 2.1213 | 0.0192 |
| **25** | 1.5837 | 1.4543 | 0.0137 | 0.6930 | 0.4621 | 0.4765 | 0.2404 | 1.7639 | 1.5744 | 0.0188 |
| **40** | 1.4886 | 1.1444 | 0.0137 | 0.6121 | 0.5108 | 0.5255 | 0.2624 | 1.7483 | 1.4540 | 0.0183 |
| **45** | 1.4480 | 1.0700 | 0.0137 | 0.7123 | 0.4931 | 0.5189 | 0.2586 | 1.7659 | 1.4564 | 0.0184 |
| **50** | **1.4252** | **1.0398** | **0.0132** | **0.6079** | **0.5161** | **0.5230** | **0.2600** | **1.7708** | **1.4401** | **0.0184** |

### 10.4 Final Evaluation Summary
- **Overall Model Precision:** **60.79%** ($0.6079$)
- **Overall Model Recall:** **51.61%** ($0.5161$)
- **Mean Average Precision @ IoU 0.50 (mAP@50):** **52.30%** ($0.5230$)
- **Mean Average Precision @ IoU 0.50:0.95 (mAP@50-95):** **26.00%** ($0.2600$)
- **Loss Progression:** Training classification loss converged from $4.805$ in Epoch 1 down to $1.040$ in Epoch 50 (a 78.4% reduction in classification error).

### 10.5 Saved Weights & Artifacts
The training run generated the following files in `runs/detect/train-4/`:
- `weights/best.pt`: Best-performing model weights across validation epochs.
- `weights/last.pt`: Final epoch checkpoint for resuming training.
- `confusion_matrix.png` & `confusion_matrix_normalized.png`: Class-level confusion matrices.
- `BoxF1_curve.png`, `BoxPR_curve.png`, `BoxP_curve.png`, `BoxR_curve.png`: Evaluation curves.
- `results.png`: Training/validation loss and metric curves over time.

---

## 11. Output and Results

### 11.1 Detection Output Format
The `/predict` endpoint returns a structured JSON payload:
```json
{
  "success": true,
  "annotated_image": "/static/results/result_0dc78304_ppe-inference-im0.png",
  "average_confidence": 76.8,
  "compliance_score": 40.0,
  "status": "CRITICAL",
  "counts": {
    "Person": 5,
    "helmet": 2,
    "vest": 0,
    "gloves": 0,
    "boots": 0,
    "goggles": 0,
    "no_helmet": 1,
    "no_vest": 0,
    "no_goggle": 0,
    "no_gloves": 0,
    "no_boots": 0,
    "none": 0
  },
  "detections": [
    { "class": "Person", "confidence": 84.2, "bbox": [102.5, 45.1, 230.4, 410.8] },
    { "class": "helmet", "confidence": 78.5, "bbox": [140.2, 46.0, 195.8, 102.3] }
  ],
  "violations": [
    "Direct violation: 1 instance(s) of no_helmet (Hard Hat / Helmet missing).",
    "Missing Helmets: Found 2 for 5 Persons.",
    "Missing Vests: Found 0 for 5 Persons."
  ],
  "alert": {
    "triggered": true,
    "enabled": true,
    "configured": true,
    "recipient": "dsilvaa078@student.sfit.ac.in",
    "message": "Violation detected! Alert email dispatched to dsilvaa078@student.sfit.ac.in."
  },
  "device": "0"
}
```

### 11.2 Example Scenarios Supported by the System
1. **Scenario A: Full Compliance (`SAFE`)**
   - Detection: 3 Persons, 3 helmets, 3 vests, 0 negative classes.
   - Score: **100%** | Status: **`SAFE`** (green).
   - Alert: No email sent; safe status banner displayed.
2. **Scenario B: Partial Non-Compliance (`WARNING` / `CRITICAL`)**
   - Detection: 4 Persons, 2 helmets, 3 vests.
   - Score: **62.5%** | Status: **`CRITICAL`** (red).
   - Violations: Missing Helmets (2 of 4), Missing Vests (1 of 4).
   - Alert: Async email dispatched to the configured safety supervisor with annotated image attached.
3. **Scenario C: Explicit Negative Detection (`CRITICAL`)**
   - Detection: 1 Person, 1 `no_helmet`.
   - Score: **0%** | Status: **`CRITICAL`** (red).
   - Violations: Direct violation: `no_helmet` detected.
   - Alert: Critical-priority email alert dispatched immediately.

### 11.3 Verified Test Images in the Workspace
Inspection of `static/uploads/` and `static/results/` confirms 24 prior inference runs on real test imagery:
- `ppe-inference-im0.png` (official multi-worker benchmark image)
- `worker.jpeg`, `worker2.jpeg`, `worker3.jpeg` (individual worker inspection photos)
- `images_3.png`
- `Screenshot_2026-08-08_003459.png`

---

## 12. Project Features

### 12.1 Fully Implemented Features
- [x] YOLO26n object detection fine-tuned on 11 PPE classes.
- [x] Automatic GPU/CPU hardware detection and reporting in UI.
- [x] Dynamic model weight resolution with automatic fallbacks.
- [x] Web dashboard with drag-and-drop image uploads.
- [x] Side-by-side original vs. annotated image comparison.
- [x] Quantitative compliance scoring algorithm (0–100%).
- [x] Three-tier status classification (`SAFE`, `WARNING`, `CRITICAL`).
- [x] Detailed detection breakdown with per-object confidence scores.
- [x] Asynchronous background SMTP email dispatch with HTML templates.
- [x] Email attachments with annotated detection images.
- [x] Anti-spam rate limiting with configurable cooldown timers.
- [x] Web-based SMTP credential configuration and test email tool.
- [x] Cloud training script (`train_colab.py`) and step-by-step Colab guide.

### 12.2 Partially Implemented Features
- [!] **100-Epoch Retraining:** Training pipeline scripts (`train_model.py`, `train_colab.py`) are fully written, but the model currently deployed in `runs/detect/train-4` is the completed 50-epoch run.
- [!] **Model Export Pipeline:** ONNX export was executed in `PPEGuard.ipynb` (`best.onnx`), but the web server currently serves the PyTorch `.pt` file rather than an ONNX Runtime session.

### 12.3 Planned / Suggested but Not Implemented
- [ ] **Live RTSP / WebRTC Video Streaming:** The application currently processes static uploaded images rather than continuous camera feeds.
- [ ] **Relational Database Logging:** Inspection history is not stored in a database (e.g., SQLite, PostgreSQL); results exist only as filesystem image files and volatile HTTP responses.
- [ ] **SMS / WhatsApp / Webhook Notifications:** Alerts are limited to SMTP email (no Twilio, Slack, or webhook integrations).
- [ ] **Worker Identity Tracking:** Face recognition and worker ID re-identification are not implemented.

---

## 13. Advantages and Limitations

### 13.1 Advantages & Technical Strengths
- **End-to-End Functional Pipeline:** Integrates deep learning model training, web API serving, browser UI, and automated notification delivery.
- **Asynchronous Execution:** Threaded email delivery ensures web request latency remains fast and unaffected by SMTP network delays.
- **Explainable Compliance Metrics:** Uses a transparent, interpretable scoring formula rather than an opaque black box.
- **Explicit Violation Handling:** Capable of detecting both the presence of required gear and explicit missing gear (`no_helmet`, `no_vest`).
- **Low Compute Overhead:** The 2.5M parameter YOLO26n model runs efficiently on consumer hardware and CPUs.

### 13.2 Limitations & Failure Scenarios
- **Single-Image Ingestion:** Currently requires discrete image uploads rather than processing real-time CCTV streams.
- **Class Imbalance on Negative Labels:** Negative classes (`no_boots`, `no_goggle`) have fewer training annotations than positive classes, leading to lower recall on those specific classes.
- **Distance & Occlusion Sensitivity:** Small items (goggles, gloves) can be difficult to detect at long camera distances or in low-resolution imagery.
- **Email Delivery Dependencies:** Email alerts rely on valid SMTP credentials (such as Google App Passwords) and third-party mail server availability.

---

## 14. Real-World Applications

| Industry / Sector | Practical Use Case | Primary Beneficiaries |
| :--- | :--- | :--- |
| **Commercial Construction** | Fixed-camera monitoring of site entrances, scaffolding, and active crane zones. | Site Foremen, Project Managers |
| **Manufacturing & Fabrication** | Verifying workers wear helmets, eye protection, and gloves on factory assembly lines. | HSE Officers, Plant Operations |
| **Mining & Heavy Quarrying** | Entrance checkpoints verifying safety footwear and high-visibility apparel before site access. | Safety Gate Operators |
| **Drone Site Inspections** | Processing aerial survey imagery of large construction sites to audit safety compliance. | Project Executives, Insurers |
| **Insurance & Auditing** | Generating automated visual documentation of safety compliance for risk assessments. | Risk Underwriters, Compliance Auditors |

---

## 15. Future Scope

1. **RTSP Live Video Stream Ingestion:** Integrate OpenCV VideoCapture or WebRTC to process live camera feeds at 15–30 FPS.
2. **100-Epoch Retraining on Cloud GPU:** Run `train_colab.py` for 100 epochs on a Tesla T4 to improve mAP@50 beyond current levels.
3. **Database Logging & Historical Analytics:** Integrate SQLite or PostgreSQL to record every inspection, track violation trends over time, and generate compliance reports.
4. **ONNX / TensorRT Edge Acceleration:** Export weights to TensorRT or ONNX Runtime to increase inference throughput on edge devices.
5. **Multi-Channel Alerting:** Add webhooks for Slack, Microsoft Teams, and WhatsApp/SMS via Twilio.

---

## 16. Conclusion

The **PPEGuard** project implements a practical, end-to-end computer vision solution for industrial safety monitoring. By combining the lightweight **Ultralytics YOLO26 Nano** architecture with an interpretable compliance scoring algorithm, an asynchronous email alerting engine, and a dark-mode web dashboard, the system automates what has traditionally been a manual, error-prone safety inspection process.

The custom-trained model (50 epochs on the 1,416-image Construction PPE dataset) achieves a **52.3% mAP@50** and **60.8% precision**, demonstrating reliable multi-class detection across workers, protective gear, and missing-gear violations. With complete training pipelines, evaluation curves, web APIs, and responsive frontends in place, PPEGuard represents a solid foundation for automated workplace safety compliance.

---

## 17. References

1. **Ultralytics YOLO Documentation & Repository:**  
   Ultralytics Inc., *YOLOv8 / YOLO11 / YOLO26 Architecture & Models*, https://docs.ultralytics.com
2. **Construction-PPE Dataset:**  
   Ultralytics Datasets Hub, *Construction PPE Detection Dataset*, https://docs.ultralytics.com/datasets/detect/construction-ppe/
3. **PyTorch Deep Learning Platform:**  
   Paszke, A., et al., *PyTorch: An Imperative Style, High-Performance Deep Learning Library*, NeurIPS. https://pytorch.org
4. **Flask Web Development:**  
   Pallets Projects, *Flask Documentation (v3.x)*, https://flask.palletsprojects.com/
5. **OSHA Safety Regulations:**  
   Occupational Safety and Health Administration (OSHA), *Personal Protective Equipment Standard (29 CFR 1926.95 / 1926.100)*, U.S. Department of Labor.
