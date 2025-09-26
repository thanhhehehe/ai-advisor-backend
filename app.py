from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Route mặc định (test)
@app.route("/")
def home():
    return "AI Advisor Backend is running!"

# Route API chính
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    return jsonify({"answer": f"Bạn vừa hỏi: {question}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
