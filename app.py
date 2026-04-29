# app.py
from flask import Flask, render_template, request
from analyzer import analyze
from generator import generate_password
from database import init_db, is_reused, save_password

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        strength, entropy, feedback = analyze(password)

        reused = is_reused(username, password)

        suggestion = None
        if strength != "Strong":
            suggestion = generate_password()

        if not reused:
            save_password(username, password)

        result = {
            "strength": strength,
            "entropy": entropy,
            "feedback": feedback,
            "reused": reused,
            "suggestion": suggestion
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)