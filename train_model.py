from ultralytics import YOLO
from pathlib import Path
import torch

def main():
    print("--- PPEGuard Retraining Pipeline ---")
    
    # Verify GPU
    is_avail = torch.cuda.is_available()
    print("CUDA Available:", is_avail)
    if is_avail:
        print("GPU Name:", torch.cuda.get_device_name(0))
        device = 0
    else:
        print("WARNING: CUDA unavailable — using CPU. This is NOT expected.")
        device = "cpu"
        
    PROJECT_DIR = Path.cwd()
    data_yaml = str(PROJECT_DIR / "datasets" / "construction-ppe" / "data.yaml")
    
    print(f"\nUsing Dataset: {data_yaml}")
    
    import argparse
    parser = argparse.ArgumentParser(description="Train PPEGuard YOLO model")
    parser.add_argument("--epochs", type=int, default=100, help="Number of epochs to train (default: 100)")
    parser.add_argument("--resume", action="store_true", help="Resume training from previous checkpoint (train-4/weights/last.pt)")
    parser.add_argument("--batch", type=int, default=16, help="Batch size (default: 16)")
    args = parser.parse_args()

    # Model selection
    last_checkpoint = PROJECT_DIR / "runs" / "detect" / "train-4" / "weights" / "last.pt"
    if args.resume and last_checkpoint.exists():
        print(f"\nResuming training from checkpoint: {last_checkpoint}")
        model = YOLO(str(last_checkpoint))
    else:
        print("\nInitializing model from base weights: yolo26n.pt")
        model = YOLO("yolo26n.pt")
    
    # Start training
    print(f"\nStarting training for {args.epochs} epochs (device: {device})...")
    results = model.train(
        data=data_yaml,
        epochs=args.epochs,
        batch=args.batch,
        imgsz=640,
        device=device,
        project="runs/detect",
        name="train-100",
    )
    
    print("\nTraining completed successfully.")

if __name__ == '__main__':
    # Fix for windows multiprocessing in script
    import multiprocessing
    multiprocessing.freeze_support()
    main()
