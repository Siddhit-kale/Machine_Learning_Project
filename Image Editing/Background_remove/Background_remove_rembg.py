# install library of Rembg
# pip install rembg 

from rembg import remove
import requests
from PIL import Image
from io import BytesIO
import os

os.makedirs('original', exist_ok=True)
os.makedirs('masked', exist_ok=True)

img_url= 'C:\Users\Siddhit\Documents\Collage Manuals\Machin Learning\Image Editing\Image\Generative_fill2.jpg';
img_name = img_url.split('/')[-1]
img_name

img = Image.open(BytesIO(requests.get(img_url).content))

