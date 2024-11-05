from backend.core.config import settings

def get_folder_id(category: str) -> str:
    folder_mapping = settings.CATEGORY_FOLDER_MAPPING
    return folder_mapping.get(category, 'default_folder_id')
