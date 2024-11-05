import os

def save_pdf_locally(pdf_content: bytes, filename: str, category: str, base_path: str) -> str:
    category_path = os.path.join(base_path, category)
    os.makedirs(category_path, exist_ok=True)
    file_path = os.path.join(category_path, filename)
    with open(file_path, 'wb') as f:
        f.write(pdf_content)
    return file_path
