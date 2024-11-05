# services/google_drive_service.py

from google.oauth2 import service_account
from googleapiclient.discovery import build
from backend.core.config import settings
import io
from googleapiclient.http import MediaIoBaseUpload

credentials = service_account.Credentials.from_service_account_file(
    settings.SERVICE_ACCOUNT_FILE, scopes=settings.SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

def save_pdf_to_drive(pdf_content: bytes, filename: str, folder_id: str) -> str:
    file_metadata = {
        'name': filename,
        'parents': [folder_id],
        'mimeType': 'application/pdf'
    }
    media = MediaIoBaseUpload(io.BytesIO(pdf_content), mimetype='application/pdf')
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    return file.get('id')
