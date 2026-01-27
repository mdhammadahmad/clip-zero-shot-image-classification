from fastapi import APIRouter, UploadFile, File
from app.image_reader import read_image
from app.clip_model import CLIPZeroShotClassifier

router = APIRouter()
classifier = CLIPZeroShotClassifier()

@router.post("/classify")
async def classify_image(
    image: UploadFile = File(...),
    labels: str = ""
):
    label_list = [l.strip() for l in labels.split(",") if l.strip()]

    img = read_image(image)
    prediction, scores = classifier.classify(img, label_list)

    return {
        "prediction": prediction,
        "scores": scores
    }
