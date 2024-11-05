from pydantic import BaseModel
from typing import Optional

class RecipeInput(BaseModel):
    text: Optional[str] = None

class RecipeResponse(BaseModel):
    message: str
    category: str
    google_drive_file_id: Optional[str] = None
    local_file_path: Optional[str] = None