# clip-zero-shot-image-classification
A FastAPI + Docker based REST API for zero-shot image classification using OpenAI CLIP.   Classify images  without training by providing natural-language labels at inference time..
=======
# CLIP Zero-Shot Image Classification API

A **FastAPI + Docker** based REST API for **zero-shot image classification** using **OpenAI CLIP**.  
Classify images **without training** by providing natural-language labels at inference time.

---

##  Features

- Zero-shot image classification using **CLIP**
- No model training required
- Accepts **custom labels** at runtime
- REST API powered by **FastAPI**
- Interactive **Swagger UI**
- Fully **Dockerized**
- Clean, modular project structure

---

## How It Works

CLIP (Contrastive Language–Image Pretraining) learns a joint embedding space for images and text.

At inference time:
- The image and the label texts are embedded
- Cosine similarity is computed
- The label with the highest similarity is selected

---

## Processing Flow (Flowchart)

~~~text

+----------------------+
|      Client          |
| (Browser / Postman)  |
+----------+-----------+
           |
           v
+----------------------------------+
|        Docker Container           |
|                                  |
|  +----------------------------+  |
|  |        FastAPI App          |  |
|  |                            |  |
|  |  POST /classify             |  |
|  |  - image (multipart)        |  |
|  |  - labels (query param)     |  |
|  +-------------+--------------+  |
|                |                 |
|                v                 |
|  +----------------------------+  |
|  |     Image Reader            |  |
|  |  (PIL / preprocessing)     |  |
|  +-------------+--------------+  |
|                |                 |
|                v                 |
|  +----------------------------+  |
|  |  CLIP Zero-Shot Classifier  |  |
|  |                            |  |
|  |  - Encode Image             |  |
|  |  - Encode Text Labels       |  |
|  |  - Cosine Similarity        |  |
|  +-------------+--------------+  |
|                |                 |
|                v                 |
|  +----------------------------+  |
|  |     Prediction Engine       |  |
|  |  - Best label               |  |
|  |  - Confidence scores        |  |
|  +-------------+--------------+  |
|                |                 |
|                v                 |
|  +----------------------------+  |
|  |     JSON Response           |  |
|  +----------------------------+  |
|                                  |
+----------------------------------+
           |
           v
+----------------------+
|    API Response      |
|  (prediction + score)|
+----------------------+

~~~

---

## Project Structure: 

~~~python

.
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── api.py               # API routes
│   ├── clip_model.py        # CLIP zero-shot classifier
│   ├── image_reader.py      # Image loading utilities
│   └── __init__.py
│
├── requirements.txt
├── Dockerfile
└── README.md

~~~

---

## Tech Stack

- Python 3.11

- FastAPI

- Uvicorn

- OpenAI CLIP

- PyTorch

- Docker

---

## Installation

1. Clone the repository:

    git clone https://github.com/<your-username>/clip-zero-shot-api.git
    cd clip-zero-shot-api

2. Build Docker image:

    docker build -t clip-api .

3. Run the container:

    docker run -p 8000:8000 clip-api

---

## Access the API

1. Swagger UI: http://localhost:8000/docs

2. Health Check: http://localhost:8000/

---

## API Usage

1. Endpoint
  
    POST /classify

2. Parameters

| Name   | Type   | Description            |
| ------ | ------ | ---------------------- |
| image  | File   | Image to classify      |
| labels | String | Comma-separated labels |

---

## EXAMPLE: 

Image : 

![Example Image](images/image.jpg)


Example Labels : cat,dog,car,person,coconut,duck

sample Response : 

~~~python

{
    "prediction": "dog",
    "scores": {
        "dog": 0.92,
        "cat": 0.04,
        "person": 0.02,
        "duck": 0.01,
        "coconut": 0.01
    }
}

~~~
---

## Author and Contact

**Author:** Mohammad Hammad Ahmad 

**Email:** mdhammadahmadgithub@gmail.com 

**LinkedIn:**  https://www.linkedin.com/in/mohammad-hammad-ahmad-188628227  

Feel free to reach out via email or on LinkedIn.

---

