from flask import Flask, jsonify
import random
import json
import os
from datetime import date

app = Flask(__name__)

# Load questions from JSON file


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "questions.json"), "r") as f:
    questions = json.load(f)

@app.route("/question/random", methods=["GET"])
def random_question():
    question = random.choice(questions)
    return jsonify(question)

@app.route("/questions", methods=["GET"])
def all_questions():
    return jsonify(questions)

@app.route("/question/<int:qid>", methods=["GET"])
def get_question(qid):
    if 0 <= qid < len(questions):
        return jsonify(questions[qid])
    return jsonify({"error": "Question not found"}), 404

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Question API! Try /question/random"
    })

@app.route("/question/daily", methods=["GET"])
def daily_question():
    # Use today's date to pick a question index
    today = date.today()
    index = today.toordinal() % len(questions)
    return jsonify(questions[index])



if __name__ == "__main__":
    app.run(debug=False)
