"""
PPEGuard 100-Epoch Retraining Pipeline for Google Colab / Kaggle / Cloud GPU
=============================================================================
This script handles:
1. GPU verification (Tesla T4 / V100 / A100)
2. Downloading & verifying the Ultralytics construction-ppe dataset
3. Training YOLO for 100 epochs with batch size 16 and imgsz 640
4. Automatically zipping best.pt weights and metrics for download to local app
"""

import os
import shutil
import zipfile
from pathlib import Path
import torch
from ultralytics import YOLO

def main():
    print("=" * 65)
    print("     PPEGuard 100-Epoch Retraining Pipeline (Colab / GPU)     ")
    print("=" * 65)

    # 1. GPU Check
    if not torch.cuda.is_available():
        print("WARNING: CUDA is NOT available! Make sure you selected a GPU runtime:")
        print("In Google Colab: Runtime -> Change runtime type -> T4 GPU")
        device = "cpu"
    else:
        gpu_name = torch.cuda.get_device_name(0)
        print(f"CUDA Available: True | Device: 0 ({gpu_name})")
        device = 0

    # 2. Dataset Setup
    # Ultralytics has built-in automatic download for construction-ppe:
    dataset_cfg = "construction-ppe.yaml"
    print(f"\nTarget Dataset Config: {dataset_cfg}")

    # 3. Model Checkpoint (Resume or Start Fresh)
    last_ckpt = Path("last.pt")
    if last_ckpt.exists():
        print(f"\nFound uploaded checkpoint '{last_ckpt}'! Resuming to 100 epochs...")
        model = YOLO(str(last_ckpt))
    else:
        print("\nStarting from base pretrained weights: yolo26n.pt")
        model = YOLO("yolo26n.pt")

    # 4. Train for 100 Epochs
    print("\nStarting training for 100 epochs (imgsz=640, batch=16)...")
    results = model.train(
        data=dataset_cfg,
        epochs=100,
        imgsz=640,
        batch=16,
        device=device,
        project="runs/detect",
        name="train-100",
        save=True,
        plots=True,
        exist_ok=True
    )

    print("\n" + "=" * 65)
    print("Training completed successfully!")
    print("=" * 65)

    # 5. Package weights and metrics for download
    save_dir = Path("runs/detect/train-100")
    weights_best = save_dir / "weights" / "best.pt"
    
    if weights_best.exists():
        size_mb = weights_best.stat().st_size / (1024 * 1024)
        print(f"\nBest weights saved at: {weights_best} ({size_mb:.2f} MB)")
        zip_path = Path("ppe_model_100epochs.zip")
        print(f"Packaging run results to {zip_path.name} ...")
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in save_dir.glob("**/*"):
                if file.is_file() and not file.name.endswith(".tmp"):
                    zipf.write(file, arcname=file.relative_to(save_dir))
        print(f"\nZip archive created successfully: {zip_path.resolve()}")
        print("\nDownload instructions for Colab:")
        print("Run in a new cell: from google.colab import files; files.download('ppe_model_100epochs.zip')")

if __name__ == "__main__":
    main()
