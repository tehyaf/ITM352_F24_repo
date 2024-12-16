from flask import Flask, render_template, request, redirect, url_for
import random
import datetime
import json

app = Flask(__name__)

def get_zodiac_sign(day, month):
    zodiac_dates = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
        ("Capricorn", (12, 22), (1, 19))
    ]
    for sign, start, end in zodiac_dates:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "Unknown"

def generate_fortune(zodiac):
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_dir, "data", "fortunes.json")

    with open(data_file_path, "r") as f:
        fortunes = json.load(f)
    return random.choice(fortunes.get(zodiac, fortunes["default"]))

def generate_lucky_numbers():
    return [random.randint(1, 100) for _ in range(5)]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        birthdate = request.form["birthdate"]
        try:
            birthdate_obj = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
            zodiac = get_zodiac_sign(birthdate_obj.day, birthdate_obj.month)
            
            return redirect(url_for("result", name=name, zodiac=zodiac))
        except ValueError:
            return render_template("index.html", error="Invalid date format. Use YYYY-MM-DD.")
    return render_template("index.html")

@app.route("/result")
def result():
    name = request.args.get("name", "Friend")
    zodiac = request.args.get("zodiac", "Unknown")

    fortune = generate_fortune(zodiac)
    lucky_numbers = generate_lucky_numbers()

    return render_template(
        "result.html",
        name=name,
        zodiac=zodiac,
        fortune=fortune,
        lucky_numbers=lucky_numbers
    )

if __name__ == "__main__":
    app.run(debug=True)
