"""
Prompt Loader — Load and use prompts programmatically.
Usage:
    from scripts.loader import get_prompt, list_categories, search_prompts
"""
import json
from pathlib import Path

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

def load_category(category):
    path = PROMPTS_DIR / (category + ".json")
    if not path.exists():
        raise FileNotFoundError(f"Category not found: {category}")
    return json.loads(path.read_text(encoding="utf-8"))

def list_categories():
    return [f.stem for f in PROMPTS_DIR.glob("*.json")]

def get_prompt(category, prompt_key, **variables):
    prompts = load_category(category)
    if prompt_key not in prompts:
        raise KeyError(f"Key not found. Available: {list(prompts.keys())}")
    return prompts[prompt_key]["template"].format(**variables)

def search_prompts(query):
    results = []
    for cat in list_categories():
        for key, data in load_category(cat).items():
            if query.lower() in (data.get("title","") + data.get("description","")).lower():
                results.append({"category": cat, "key": key, "title": data.get("title","")})
    return results

if __name__ == "__main__":
    print("Categories:", list_categories())
    print("Search 'code':", search_prompts("code"))
