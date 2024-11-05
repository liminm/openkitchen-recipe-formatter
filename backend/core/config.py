from pydantic_settings import BaseSettings
from typing import Dict

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    SERVICE_ACCOUNT_FILE: str
    SCOPES: list = ['https://www.googleapis.com/auth/drive']
    # TODO fill out with corresponding dirs; broken right now
    CATEGORY_FOLDER_MAPPING: Dict[str, str] = {
        "Baking": "folder_id_baking",
        "Salads",
        "Mains",
        "Desserts",
        "Appetizers"
        "Noodles",
        "Rice",
        "Fruits",
        "Sweets",
        "Snacks",
        "Drinks",
    }
    CATEGORIES: list = [
        "Baking",
        "Salads",
        "Mains",
        "Desserts",
        "Appetizers"
        "Noodles",
        "Rice",
        "Fruits",
        "Sweets",
        "Snacks",
        "Drinks",
    ]
    LOCAL_SAVE_PATH: str = "saved_recipes"

    class Config:
        env_file = ".env"

settings = Settings()
