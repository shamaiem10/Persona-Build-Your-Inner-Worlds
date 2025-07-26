# huggingface_api.py
import os
import requests
from dotenv import load_dotenv

# 🌿 Load secrets from .env file
load_dotenv()

# 🛡 Securely fetch the Hugging Face token
HF_TOKEN = os.getenv("HF_TOKEN")

# ✅ Setup API configuration
API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def ask_persona(prompt):
    payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "model": "Qwen/Qwen3-Coder-480B-A35B-Instruct:novita"
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        # 🔍 Debugging: show full response if needed
        print("⚠️ RAW RESPONSE:")
        print(response.text)

        # 🛡 Check for valid JSON
        if "application/json" not in response.headers.get("Content-Type", ""):
            return "[Error]: Server did not return JSON. Possibly an HTML error page."

        response.raise_for_status()
        data = response.json()

        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"[Error]: {e}"
