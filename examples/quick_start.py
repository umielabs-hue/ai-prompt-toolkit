"""
Quick Start — AI Prompt Toolkit
"""
import sys; sys.path.insert(0, "..")
from scripts.loader import get_prompt, list_categories, search_prompts

print("=== AI Prompt Toolkit Quick Start ===")
print("Categories:", list_categories())

# Get a prompt with variables filled in
prompt = get_prompt("development", "code_review",
    language="Python",
    code="def add(a, b): return a+b"
)
print("\nCode Review Prompt (first 200 chars):")
print(prompt[:200], "...")

# Search for marketing prompts
print("\nMarketing prompts:")
for r in search_prompts("ad"):
    print(f"  [{r['category']}] {r['key']}: {r['title']}")
