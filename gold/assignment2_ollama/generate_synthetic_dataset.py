import torch
from diffusers import StableDiffusionPipeline
from pathlib import Path

CLASSES = {
    "car": "a realistic photo of a car on the street",
    "truck": "a realistic photo of a truck on the road",
    "bicycle": "a realistic photo of a bicycle parked or being ridden",
    "pedestrian": "a realistic photo of a pedestrian walking on a sidewalk"
}

IMAGES_PER_CLASS = 10  # puedes subirlo después

def ensure_dirs():
    for split in ["train", "val"]:
        for cls in CLASSES.keys():
            Path(f"data/{split}/{cls}").mkdir(parents=True, exist_ok=True)

def main():
    ensure_dirs()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32
    ).to(device)

    for cls, prompt in CLASSES.items():
        print(f"\nGenerating images for: {cls}")

        for i in range(IMAGES_PER_CLASS):
            split = "train" if i < int(IMAGES_PER_CLASS * 0.8) else "val"
            out_path = f"data/{split}/{cls}/{cls}_{i}.png"

            image = pipe(prompt, num_inference_steps=25).images[0]
            image.save(out_path)

            print(f"  ✓ {out_path}")

if __name__ == "__main__":
    main()
