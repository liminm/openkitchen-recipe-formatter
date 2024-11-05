from typing import List

from openai import OpenAI

from backend.core.config import settings

# Access the environment variable
if settings.OPENAI_API_KEY is not None:
    print("Loaded OPENAI_API_KEY")
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
else:
    print("Something went wrong; Make sure you have added the OPENAI_API_KEY in the .env file")


def standardize_recipe(text: str) -> str:
    prompt = f"""
    You are an expert RECIPE standardizer and formatter.
    You have been given a RECIPE in a non-standard format.
    Structure the output in a nice way and include line breaks should sentences get too long.
    Each sentence should easily fit in a single line.
    Convert the following RECIPE into the standard format:

    RECIPE:
    {text}

    The standard format is:
    - Title
    - Ingredients (list)
    - Instructions (step-by-step)
    """
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0
    )
    return response.choices[0].message.content.strip()


def categorize_recipe(text: str, categories: List[str]) -> str:
    prompt = f"""
    You are an expert categorizer for recipes.
    You have been given a RECIPE and you need to categorize it into one of the following CATEGORIES: {', '.join(categories)}.    
    Output only the category name.

    RECIPE:
    {text}

    Category:
    """
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5,
        temperature=0
    )
    return response.choices[0].message.content.strip()
