from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "PASTE_YOUR_FREE_KEY_HERE")

def ask_ai_brain(message):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are Cratos-Bee-AI, a helpful, funny Kenyan AI assistant made by Joaki Thuku."},
            {"role": "user", "content": message}
        ]
    }
    try:
        r = requests.post(url, headers=headers, json=data, timeout=20)
        j = r.json()
        return j["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}."

@app.route("/")
def home():
    return "Cratos-Bee-AI is ONLINE!"

@app.route("/talk", methods=["POST"])
def talk():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = ask_ai_brain(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
  
