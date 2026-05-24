import torch
from torchvision import transforms, models
from PIL import Image

def load_model(model_path="resnet18_finetuned.pth", num_classes=4):
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()
    return model

def predict(image_path, model, class_names):
    device = "cpu"
    model.to(device)

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    image = Image.open(image_path).convert("RGB")
    tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(tensor)
        _, predicted = outputs.max(1)

    return class_names[predicted.item()]

if __name__ == "__main__":
    class_names = ["bicycle", "car", "pedestrian", "truck"]  # modify as needed
    model = load_model(num_classes=len(class_names))

    result = predict("gold/assignment1_resnet/test.jpg", model, class_names)
    print("Prediction:", result)
