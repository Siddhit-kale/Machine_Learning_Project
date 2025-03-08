import torch
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image
import requests
import numpy as np

# Load the pre-trained inpainting model
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)

# Load input image and mask
def load_image(url):
    return Image.open(requests.get(url, stream=True).raw).convert("RGB")

image_url = "Genrative_fill2.jpg"  # Provide your own image
mask_url = "https://your-image-url.com/mask.png"  # Provide a binary mask (white = keep, black = fill)

image = load_image(image_url)
mask = load_image(mask_url)

# Run the inpainting model
output = pipe(prompt="Fill the missing part realistically", image=image, mask_image=mask).images[0]

# Save and display the result
output.save("output_filled.png")
output.show()
