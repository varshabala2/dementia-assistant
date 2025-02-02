from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from database import get_db
from models import create_reminder, get_all_reminders, mark_reminder_completed
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

# app routes


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AI Companion Backend Running!"})

# reminder routes


@app.route("/set_reminder", methods=["POST"])
def set_reminder():
    data = request.json
    create_reminder(data["text"], data["time"])
    return jsonify({"message": "Reminder Set!"})


@app.route("/get_reminders", methods=["GET"])
def get_reminders():
    return jsonify(get_all_reminders())


@app.route("/complete_reminder", methods=["POST"])
def complete_reminder():
    data = request.json
    mark_reminder_completed(data["text"])
    return jsonify({"message": "Reminder Completed!"})

# ai routes


@app.route("/chat_with_ai", methods=["POST"])
def chat_with_ai():
    data = request.json
    user_message = data["message"]

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_message}]
    )

    ai_response = response["choices"][0]["message"]["content"]
    return jsonify({"reply": ai_response})

# Test route


@app.route('/api/test', methods=['GET'])
def test_connection():
    return jsonify({"message": "Connection successful!"})


# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
