# Contributing to AI Prompt Toolkit

## Adding a Prompt

1. Find the right category JSON in `prompts/`
2. Add your prompt:
```json
{
  "your_key": {
    "title": "Human Readable Title",
    "description": "What this does",
    "variables": ["var1", "var2"],
    "template": "Your prompt with {var1} placeholders"
  }
}
```
3. Test: `python scripts/loader.py`
4. Submit a PR

## Guidelines

- Prompts must be tested against at least one LLM
- List all required variables
- Write clear descriptions
- Prefer specific over generic prompts
