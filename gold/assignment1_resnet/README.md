# Gold Assignment 1 — ResNet18 Fine‑Tuning

This module contains the implementation of a complete transfer‑learning pipeline using **ResNet18**.

## Contents
- `resnet_finetuning.ipynb`: Notebook for training and evaluation.
- `train_resnet.py`: Script version of the training pipeline.
- `inference.py`: Script for running predictions on new images.
- `data/`: Placeholder folder (datasets are not included in the repository).

## Features
- Image preprocessing and augmentation
- Transfer learning with frozen backbone
- Custom classification head
- Training loop with loss tracking
- Inference utilities

## How to Run

### Local
1. Activate your virtual environment  
2. Install dependencies  
3. Run the notebook or:

python train_resnet.py


### Google Colab
Upload the notebook and mount your dataset.

## Dataset Structure

data/
├── train/
└── val/


## Notes
Datasets are not included in the repository.