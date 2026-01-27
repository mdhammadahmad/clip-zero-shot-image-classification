from PIL import Image
from fastapi import UploadFile

def read_image(upload_file: UploadFile) -> Image.Image:
    image = Image.open(upload_file.file)
    return image.convert("RGB")
