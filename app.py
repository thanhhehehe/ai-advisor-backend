from flask import Flask, request, jsonify
from flask_cors import CORS
import os, openai

app = Flask(__name__)
CORS(app)  # <--- bắt buộc có dòng này

# Lấy API Key từ biến môi trường Render
openai.api_key = os.environ.get("sk-...p04A")

# Route test
@app.route("/")
def home():
    return "✅ AI Advisor Backend is running!"

# Route chính để hỏi AI
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Thiếu câu hỏi"}), 400

    try:
        # Gọi OpenAI API (ví dụ GPT-4o-mini)
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Bạn là cố vấn học tập AI, giúp giải thích dễ hiểu."},
                {"role": "user", "content": question}
            ]
        )
        answer = response["choices"][0]["message"]["content"]

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


