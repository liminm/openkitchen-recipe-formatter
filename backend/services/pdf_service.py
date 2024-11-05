from pdfminer.high_level import extract_text
from weasyprint import HTML
import tempfile
import os

import re


def parse_standardized_recipe(text: str) -> dict:
    """
    Parses the standardized recipe text into its components.
    """
    title_match = re.search(r"Title:\s*(.+)", text)
    ingredients_match = re.search(r"Ingredients:\s*((?:- .+\n?)*)", text, re.MULTILINE)
    instructions_match = re.search(r"Instructions:\s*((?:\d+\..+\n?)*)", text, re.MULTILINE)

    title = title_match.group(1).strip() if title_match else "Untitled Recipe"

    ingredients = []
    if ingredients_match:
        ingredients_text = ingredients_match.group(1)
        ingredients = [line.strip("- ").strip() for line in ingredients_text.strip().split("\n") if line.strip()]

    instructions = []
    if instructions_match:
        instructions_text = instructions_match.group(1)
        instructions = [line.strip().split(". ", 1)[1].strip() for line in instructions_text.strip().split("\n") if
                        line.strip()]

    return {
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions
    }


def extract_text_from_pdf(file_content: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file_content)
        tmp_file_path = tmp_file.name
    text = extract_text(tmp_file_path)
    os.unlink(tmp_file_path)
    return text

def generate_pdf_from_text(text: str) -> bytes:
    html_content = f"<pre>{text}</pre>"
    pdf_file = HTML(string=html_content).write_pdf()
    return pdf_file
