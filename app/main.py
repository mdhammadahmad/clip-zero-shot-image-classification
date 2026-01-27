from fastapi import FastAPI
from app.api import router

def create_app() -> FastAPI:
    app = FastAPI(title="CLIP Zero-Shot Image Classification API")
    app.include_router(router)
    return app

app = create_app()
