from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import random
from database import get_db
from models import create_reminder, get_all_reminders, mark_reminder_completed
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

#app routes

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AI Companion Backend Running!"})

#reminder routes

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

#ai routes

#mnemo intro

# Function to introduce Mnemo
def get_mnemo_intro():
    return "Hello! My name is Mnemo, your AI powered assistant. I’m here to assist you with your memory and have fun playing games with you. If you ever want to play a game, just let me know!"

#ai chat bot

# Use the new API structure
def get_ai_response(user_message):
    # Define the system-level prompt for context
    system_message = """
    You are Mnemo, a friendly and helpful assistant designed to support people with dementia. 
    Your responses should always be patient, kind, and understanding. 
    Respond to all user messages in a way that encourages them and provides cognitive stimulation.
    If the user asks to play a game, offer them a selection of games, and make sure to engage them with positive feedback.
    """

    # Now use the OpenAI ChatCompletion API
    #old is ChatCompletion new is openai.chat_completions.create()
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # The model you're using
        messages=[
            {"role": "system", "content": system_message},  # System-level context
            {"role": "user", "content": user_message}      # User's message
        ]
    )

    ai_response = response.choices[0].message.content.strip()
    return ai_response

# Function to handle game request
def handle_game_request(user_message):
    trigger_keywords = ["play a game", "let's play", "game time", "Mnemo, play"]
    
    if any(keyword in user_message.lower() for keyword in trigger_keywords):
        return """
        I’d love to play a game with you! Here are a few fun options:
        
        1️⃣ **Daily Word Association**: I'll give you a word, and you respond with a related word.
        2️⃣ **Fill in the Blank**: I’ll give you a common phrase with a blank, and you fill it in!
        3️⃣ **Story Completion**: I’ll start a story, and you can finish it!
        4️⃣ **Personalized Memory Recall**: I’ll show you a photo or memory, and you tell me what you remember.
        5️⃣ **Music & Lyrics Recall**: I'll play a snippet of a song, and you continue the lyrics!

        Just let me know which game you'd like to play, and we’ll get started! 😊
        """
    else:
        return get_ai_response(user_message)  # If no game request, continue normal conversation

# Cognitive Game - Daily Word Association
def word_association_game():
    words = ["Sun", "Tree", "Ocean", "Mountain", "Sky"]
    word_to_start = random.choice(words)
    return f"Let's play Word Association! I'll start with the word: {word_to_start}. What word comes to your mind?"

# Cognitive Game - Fill in the Blank
def fill_in_the_blank_game():
    phrases = [
        "An apple a day keeps the ___ away.",
        "Actions speak louder than ___.",
        "It's ___ cats and dogs."
    ]
    phrase_to_present = random.choice(phrases)
    return f"Fill in the blank: {phrase_to_present}"

# Cognitive Game - Story Completion
def story_completion_game():
    story_start = "One day, Sarah found a lost puppy. She decided to..."
    return f"Let's play Story Completion! Here's the beginning of a story: {story_start} How would you continue it?"

# Cognitive Game - Personalized Memory Recall
def personalized_memory_game():
    # This would ideally be integrated with actual memory prompts
    memory_prompt = "This is you at the beach in 2019! Do you remember what you loved most about that trip?"
    return memory_prompt

# Cognitive Game - Music & Lyrics Recall
def music_lyrics_game():
    song_snippet = "You are my sunshine, my only sunshine..."
    return f"Let's play Music & Lyrics Recall! Can you continue the lyrics? 🎶 {song_snippet}"

# Main chat function
@app.route("/chat_with_ai", methods=["POST"])
def chat_with_ai_endpoint():
    data = request.json
    user_message = data["message"]

    # First, check if the user wants to play a game
    game_response = handle_game_request(user_message)
    if game_response:
        return jsonify({"reply": game_response})

    # If not a game request, proceed with regular conversation
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Or whichever model you are using
        messages=[{"role": "user", "content": user_message}]
    )

    ai_response = response.choices[0].message.content.strip()
    return jsonify({"reply": ai_response})

# Endpoint for getting Mnemo's introduction
@app.route("/get_mnemo_intro", methods=["GET"])
def get_mnemo_intro_endpoint():
    return jsonify({"reply": get_mnemo_intro()})

if __name__ == "__main__":
    app.run(debug=True)
