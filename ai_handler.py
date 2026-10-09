import os
import json
from openai import OpenAI

# Initialize the AI Client 
# (Make sure to set your system environment variable tomorrow, or paste your API key here for local testing)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "YOUR_PAID_OR_FREE_HACKATHON_KEY_HERE"))

# 1. CORE PROMPT blueprints designed to return exact JSON matching the app schemas
REQUIREMENTS_SYSTEM_PROMPT = """
You are a Product Manager Copilot. Your job is to take a product idea and break it down.
You MUST output ONLY a valid JSON array containing exactly 2 items: one Functional Requirement and one Non-Functional Requirement.
Do not include any conversational text, notes, markdown blocks, or backticks (```).

Follow this exact JSON structure:
[
  {"id": "FR-01", "type": "functional", "description": "Description of what the user can do"},
  {"id": "NFR-01", "type": "non-functional", "description": "Description of how the system performs"}
]
"""

# 2. Function to turn an idea into structured requirements
def generate_requirements_from_idea(product_idea):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Using a lightweight, affordable model optimal for a hackathon build
            messages=[
                {"role": "system", "content": REQUIREMENTS_SYSTEM_PROMPT},
                {"role": "user", "content": f"Product Idea: {product_idea}"}
            ],
            temperature=0.2 # Lower temperature keeps outputs predictable and strictly adhering to the schema
        )
        
        # Clean and extract raw string content
        raw_output = response.choices[0].message.content.strip()
        
        # Test if it's valid JSON
        parsed_json = json.loads(raw_output)
        return parsed_json
        
    except Exception as e:
        print(f"Error calling AI API: {e}")
        # Fallback sample data matching the presentation demo data layout if API fails
        return [
            {"id": "FR-01", "type": "functional", "description": "Students browse canteens and menus in real time."},
            {"id": "NFR-01", "type": "non-functional", "description": "Order page loads fast on campus Wi-Fi."}
        ]
 
# --- Day 1 Execution Test Execution Check ---
if __name__ == "_main_":
    print("Testing Day 1 AI Handler Blueprint...")
    test_idea = "A college food delivery application"
    result = generate_requirements_from_idea(test_idea)
    print("\nGenerated AI Output:")
    print(json.dumps(result, indent=2))