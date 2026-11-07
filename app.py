from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
# 模型下拉选项
MODEL_LIST = [
    {"name": "deepseek-chat", "display": "DeepSeek Chat 通用对话"},
    {"name": "deepseek-coder", "display": "DeepSeek Coder 代码模式"}
]

@app.route('/')
def index():
    return render_template("index.html", models=MODEL_LIST)

@app.route('/api/chat', methods=["POST"])
def chat():
    data = request.get_json()
    api_key = data.get("api_key")
    model_name = data.get("model")
    prompt = data.get("prompt")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    resp = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(debug=True)