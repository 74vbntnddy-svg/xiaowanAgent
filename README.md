# XiaoWan Agent

XiaoWan Agent is a lightweight local web AI assistant powered by the DeepSeek API. It supports model selection, code generation, and a clean browser-based interface.

## Features
- Multi-model DeepSeek selection
- Code generation and creative prompting
- Browser-based chat UI
- API key input or environment variable configuration
- Basic health check endpoint

## Quick Start

1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies

```bash
pip install flask requests
```

3. Start the app

```bash
export DEEPSEEK_API_KEY="your_api_key_here"
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

You can also paste the API key directly in the UI if you prefer not to set an environment variable.

## Configuration

The app supports these environment variables:

```bash
export DEEPSEEK_API_KEY="your_key"
export DEEPSEEK_API_URL="https://api.deepseek.com/v1/chat/completions"
```

## Project Structure

```text
.
├── app.py
├── README.md
├── templates/
│   └── index.html
└── LICENSE
```

## Notes

This project is intentionally simple and easy to extend. If you want, the next improvements could include:
- Chat history
- Streaming responses
- Session persistence
- Local ADB / PC automation features
- Better error logging and deployment configuration
