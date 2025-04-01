from flask import Flask, render_template, request, jsonify
import requests
import os
import dotenv 
dotenv.load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your_openrouter_api_key")
app = Flask(__name__)
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

def call_openrouter(prompt):
    """
    Send a request to OpenRouter's API to process the given prompt.
    """
    data = {
        "model": "deepseek/deepseek-r1-zero:free",  # Replace with the desired OpenRouter model
        "messages": [{"role": "system", "content": prompt}],
        "temperature": 0.7
    }
    try:
        response = requests.post(OPENROUTER_API_URL, json=data, headers=headers)
        response.raise_for_status()
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
    except Exception as e:
        raise Exception(f"OpenRouter API Error: {e}")

def remove_comments(code_snippet):
    """
    Remove comments from the provided code snippet using OpenRouter API.
    """
    prompt = f"""Remove all comments from the provided code snippet while retaining the lines where the comments are located. 
    Ensure the code remains clean and readable. 
    Format it properly for better clarity, but avoid adding any LaTeX-style formatting or special symbols like \\boxed{{}}. 
    Provide the raw, unformatted code only.
    {code_snippet}
    Respond with the uncommented code. Do not include any other text."""
    
    return call_openrouter(prompt)


def add_comments(code_snippet):
    """
    Generate and add comments to the provided code snippet using OpenRouter API.
    """
    prompt = f"""Analyze the following code snippet and insert detailed, beginner-friendly comments directly above each relevant line of code. 
    Ensure the comments are clear, concise, and provide insights without modifying the code's indentation, format, or structure. 
    Avoid adding any LaTeX-style formatting or special symbols like \\boxed{{}}. 
    The response should be a complete, properly formatted Python code snippet that can be copied and executed without adjustment.
    Preserve indentation strictly.
    {code_snippet}
    Respond with the commented code. Do not include any other text."""
    
    return call_openrouter(prompt)


def fix_code(code_snippet):
    prompt = f"Debug and fix errors in this code snippet:\n{code_snippet}\n"
    return call_openrouter(prompt)

@app.route('/fix', methods=['POST'])
def fix():
    data = request.json
    code_snippet = data.get("code", "")
    if not code_snippet.strip():
        return jsonify({"error": "Code snippet cannot be empty."}), 400
    try:
        fixed_code = fix_code(code_snippet)
        return jsonify({"fixed_code": fixed_code})
    except Exception as e:
        return jsonify({"error": "Failed to fix the code.", "details": str(e)}), 500


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uncomment', methods=['POST'])
def uncomment_code():
    data = request.json
    code_snippet = data.get("code", "")
    if not code_snippet.strip():
        return jsonify({"error": "Code snippet cannot be empty."}), 400
    try:
        uncommented_code = remove_comments(code_snippet)
        return jsonify({"uncommented_code": uncommented_code})
    except Exception as e:
        return jsonify({"error": "Failed to remove comments.", "details": str(e)}), 500

@app.route('/comment', methods=['POST'])
def comment_code():
    data = request.json
    code_snippet = data.get("code", "")
    if not code_snippet.strip():
         return jsonify({"error": "Code snippet cannot be empty."}), 400
    try:
        commented_code = add_comments(code_snippet)
        return jsonify({"commented_code": commented_code})
    except Exception as e:
        return jsonify({"error": "Failed to add comments.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
