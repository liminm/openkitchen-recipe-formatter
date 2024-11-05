# app/routers/recipe.py

from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from typing import Optional
from backend.services.pdf_service import extract_text_from_pdf, generate_pdf_from_text
from backend.services.openai_service import standardize_recipe, categorize_recipe
from backend.services.google_drive_service import save_pdf_to_drive
from backend.utils.categorization import get_folder_id
from backend.utils.file_operations import save_pdf_locally
from backend.models.schemas import RecipeResponse
from backend.core.config import settings
import uuid

router = APIRouter()

@router.post("/upload-recipe/", response_model=RecipeResponse)
async def upload_recipe(
    text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    save_to_drive: bool = Form(True),
    save_locally: bool = Form(True)
):
    if not text and not file:
        raise HTTPException(status_code=400, detail="No input provided")

    if file:
        if file.content_type == 'application/pdf':
            file_content = await file.read()
            extracted_text = extract_text_from_pdf(file_content)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
    else:
        extracted_text = text

    try:
        standardized_recipe = standardize_recipe(extracted_text)
        category = categorize_recipe(standardized_recipe, settings.CATEGORIES)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    pdf_content = generate_pdf_from_text(standardized_recipe)
    folder_id = get_folder_id(category)

    filename = f"{uuid.uuid4()}.pdf"

    response_data = {
        "message": "Recipe uploaded and processed successfully",
        "category": category,
        "google_drive_file_id": None,
        "local_file_path": None
    }

    if save_to_drive:
        try:
            drive_file_id = save_pdf_to_drive(pdf_content, filename, folder_id)
            response_data["google_drive_file_id"] = drive_file_id
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to save to Google Drive: {str(e)}")

    if save_locally:
        try:
            local_file_path = save_pdf_locally(
                pdf_content,
                filename,
                category,
                settings.LOCAL_SAVE_PATH
            )
            response_data["local_file_path"] = local_file_path
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to save locally: {str(e)}")

    return response_data
