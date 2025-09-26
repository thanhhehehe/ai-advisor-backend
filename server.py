from flask import Flask, request, jsonify
import requests, os
from flask_cors import CORS  # Cho phép frontend khác domain gọi API

app = Flask(__name__)
CORS(app)  # mở CORS để frontend truy cập
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    q = data.get("question", "")
    
    # Gọi OpenAI API
    resp = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENAI_KEY}"},
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role":"user","content": q}]
        }
    )
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
