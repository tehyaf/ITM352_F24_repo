import random
import json
from flask import Flask, render_template, request, redirect, url_for, session

# begin flask app
app = Flask(__name__)
app.secret_key = "secret_key_for_session" 

# Get questions from JSON file
def load_questions():
    """Load quiz questions from a JSON file."""
    with open("quiz_questions.json", "r") as file:
        data = json.load(file)
    return data["questions"]

# Routing home page
@app.route("/")
def home():
    return render_template("index.html")

# Routing quiz page
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Display one question at a time and provide feedback."""
    questions = load_questions()  # for questions from JSON

    # Begins game
    if "current_index" not in session:
        session["current_index"] = 0
        session["score"] = 0

    # current question
    current_index = session["current_index"]

    # Redirect to /result if the quiz is over
    if current_index >= len(questions):
        return redirect(url_for("result", score=session["score"]))

    # Deals with POST when answer is submitted
    if request.method == "POST":
        # Recieves answer and determines if correct
        user_answer = request.form.get("answer")
        correct_answer = questions[current_index]["correct"]

        # Determine feedback
        if user_answer == correct_answer:
            session["score"] += 1
            feedback = "Correct!"
        else:
            feedback = f"Incorrect! The correct answer was: {correct_answer}."

        # Prepare explanation 
        explanation = f"You chose '{user_answer}', but the correct answer is '{correct_answer}'." if user_answer != correct_answer else "Great job!"

        
        session["current_index"] += 1

        # returns feedback
        return render_template("question_result.html", feedback=feedback, explanation=explanation)

    # GET request
    question = questions[current_index]
    progress = (current_index + 1) / len(questions) * 100

    return render_template(
        "quiz.html",
        question=question,
        index=current_index + 1,
        total=len(questions),
        progress=progress,
    )


@app.route("/result")
def result():
    """Display the user's score and allow restarting the quiz."""
    score = request.args.get("score", 0, type=int)
    total_questions = len(load_questions())
    
    # This clears session to reset the quiz
    session.clear()
    
    return render_template("result.html", score=score, total=total_questions)

if __name__ == "__main__":
    app.run(debug=True, port=5001)




