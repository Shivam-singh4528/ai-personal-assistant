
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq
import os

app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# Create Groq client only when the key is available
client = Groq(api_key=api_key) if api_key else None

# Model available through Groq; access and limits depend on your account
MODEL_NAME = "openai/gpt-oss-20b"


@app.route("/")
def home():
    return render_template("index.html")


def get_ai_response(prompt, system_message):
    if client is None:
        raise ValueError(
            "GROQ_API_KEY nahi mili. Project ki .env file check karo."
        )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens=1024
    )

    answer = response.choices[0].message.content

    if not answer:
        return "AI ne koi text response nahi diya."

    return answer.strip()


@app.route("/ask", methods=["POST"])
def ask():
    try:
        question = request.form.get("question", "").strip()

        if not question:
            return jsonify({
                "error": "Please enter a question."
            }), 400

        answer = get_ai_response(
            question,
            "You are a helpful personal assistant. "
            "Answer clearly and simply."
        )

        return jsonify({"response": answer}), 200

    except Exception:
        app.logger.exception("Error in /ask")

        return jsonify({
            "error": (
                "AI request failed. Check the VS Code terminal "
                "for the actual error."
            )
        }), 500


@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        email_text = request.form.get("email", "").strip()

        if not email_text:
            return jsonify({
                "error": "Please paste an email first."
            }), 400

        prompt = (
            "Summarize this email in 2-3 sentences. "
            "Preserve its main purpose and important details:\n\n"
            + email_text
        )

        summary = get_ai_response(
            prompt,
            "You are an expert email assistant."
        )

        return jsonify({"response": summary}), 200

    except Exception:
        app.logger.exception("Error in /summarize")

        return jsonify({
            "error": (
                "Email summarization failed. Check the VS Code "
                "terminal for the actual error."
            )
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
