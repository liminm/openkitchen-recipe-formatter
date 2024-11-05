# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routers import recipe
from pydantic_settings import BaseSettings
from typing import Dict

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    SERVICE_ACCOUNT_FILE: str
    SCOPES: list = ['https://www.googleapis.com/auth/drive']
    CATEGORY_FOLDER_MAPPING: Dict[str, str] = {
        "Baking": "folder_id_baking",
        "Salads": "folder_id_salads",
        "Mains": "folder_id_mains",
        "Desserts": "folder_id_desserts",
        "Appetizers": "folder_id_appetizers"
    }
    CATEGORIES: list = [
        "Baking",
        "Salads",
        "Mains",
        "Desserts",
        "Appetizers",
        "Noodles",
        "Rice",
        "Fruits",
        "Sweets",
        "Snacks",
        "Drinks",
    ]
    LOCAL_SAVE_PATH: str = "./saved_recipes"

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(
    title="Recipe Uploader API",
    description="An API to upload and process recipes.",
    version="1.0.0"
)

# Configure CORS
origins = [
    "http://localhost:3000",  # React frontend
    # Add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allow specific origins
    allow_credentials=True,           # Allow cookies and authorization headers
    allow_methods=["*"],              # Allow all HTTP methods
    allow_headers=["*"],              # Allow all HTTP headers
)

# Include your API router
app.include_router(recipe.router)
