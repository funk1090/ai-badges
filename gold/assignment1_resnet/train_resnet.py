import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models
import argparse

def get_data_loaders(data_dir, batch_size):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    train_ds = datasets.ImageFolder(f"{data_dir}/train", transform=transform)
    val_ds = datasets.ImageFolder(f"{data_dir}/val", transform=transform)

    return (
        DataLoader(train_ds, batch_size=batch_size, shuffle=True),
        DataLoader(val_ds, batch_size=batch_size)
    )

def train(model, train_loader, val_loader, device, epochs):
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.fc.parameters(), lr=1e-3)

    for epoch in range(epochs):
        model.train()
        total_loss = 0

        for imgs, labels in train_loader:
            imgs, labels = imgs.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch+1}/{epochs} - Loss: {total_loss:.4f}")

    torch.save(model.state_dict(), "resnet18_finetuned.pth")
    print("Modelo guardado como resnet_finetuned.pth")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="gold/assignment1_resnet/data")
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch_size", type=int, default=16)
    args = parser.parse_args()

    device = "cpu"

    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    for param in model.parameters():
        param.requires_grad = False

    model.fc = nn.Linear(model.fc.in_features, 4)
    model = model.to(device)

    train_loader, val_loader = get_data_loaders(args.data_dir, args.batch_size)
    train(model, train_loader, val_loader, device, args.epochs)

if __name__ == "__main__":
    main()
