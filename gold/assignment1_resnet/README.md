# Gold Assignment 1 — ResNet18 Fine‑Tuning

This module implements a complete transfer‑learning pipeline using **ResNet18** to classify four classes:
**car, truck, bicycle, pedestrian**.

The project includes:
- Dataset loading using `ImageFolder`
- Transfer learning with a pretrained ResNet18
- Custom classification head (4 classes)
- Training loop with loss tracking
- CPU‑based inference pipeline
- Saved fine‑tuned model (`resnet_finetuned.pth`)

---

## 📁 Repository Contents

- `train_resnet.py` — Training script (CPU‑compatible)
- `inference.py` — Script for running predictions on new images
- `resnet_finetuned.pth` — Fine‑tuned model weights
- `README.md` — Documentation (this file)

> **Note:**  
> The dataset is **not included** in this repository due to licensing restrictions.  
> The folder `data/` is expected to exist locally when running the training script.

---

## 🧠 Model Overview

The model uses:
- **ResNet18 pretrained on ImageNet**
- Frozen backbone
- Custom final layer: `nn.Linear(512, 4)`
- Cross‑entropy loss
- Adam optimizer

Training was performed on **CPU** due to lack of CUDA support for RTX 5080 in current PyTorch builds.

---

## 📦 Dataset Structure (expected locally)

data/
├── train/
│   ├── car/
│   ├── truck/
│   ├── bicycle/
│   └── pedestrian/
└── val/
├── car/
├── truck/
├── bicycle/
└── pedestrian/


Images must be placed manually by the user.

---

## ▶️ How to Run Training

1. Activate your virtual environment  
2. Install dependencies:

pip install -r requirements.txt

3. Run training:

python train_resnet.py


This will:
- Load the dataset
- Train for 5 epochs (default)
- Save the model as `resnet_finetuned.pth`

---

## 🔍 Running Inference

Place a test image in the same folder as `inference.py`, then run:

python inference.py

Output example:

Prediction: car

---

## 📝 Notes

- The dataset is **not included** in this repository.
- Images used for training were downloaded manually and are not redistributed due to licensing.
- The model was trained on CPU because current PyTorch builds do not support RTX 5080 (sm_120).
- This implementation fulfills the requirements of **Gold Assignment 1**.