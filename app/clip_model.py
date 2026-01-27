import torch
from transformers import CLIPModel, CLIPProcessor

MODEL_NAME = "openai/clip-vit-base-patch32"

class CLIPZeroShotClassifier:
    def __init__(self):
        self.model = CLIPModel.from_pretrained(MODEL_NAME)
        self.processor = CLIPProcessor.from_pretrained(MODEL_NAME)

    def classify(self, image, labels):
        text_inputs = [f"a photo of {label}" for label in labels]

        inputs = self.processor(
            text=text_inputs,
            images=image,
            return_tensors="pt",
            padding=True
        )

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits_per_image
            probs = logits.softmax(dim=1)[0]

        scores = {
            label: float(prob)
            for label, prob in zip(labels, probs)
        }

        best_label = labels[probs.argmax().item()]

        return best_label, scores
