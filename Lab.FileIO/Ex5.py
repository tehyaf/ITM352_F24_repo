import json

# Dictionary of quiz questions from Assignment 1
quiz_data = {
    "questions": [
        {
            "question": "What year was the first email sent",
            "options": ["1971", "1985", "1990", "1965"],
            "correct": "1971"
        },
        {
            "question": "Which country is the largest producer of coffee in the world",
            "options": ["Colombia", "Ethiopia", "Brazil", "Vietnam"],
            "correct": "Brazil"
        },
        {
            "question": "What is the title of Kanye West's debut album, released in 2004",
            "options": ["Graduation", "The College Dropout", "Late Registration", "808s & Heartbreak"],
            "correct": "The College Dropout"
        },
        {
            "question": "Which iconic TV show is known for the line, 'Winter is Coming'",
            "options": ["Once Upon a Time", "Game of Thrones", "The Sopranos", "Succession"],
            "correct": "Game of Thrones"
        },
        {
            "question": "Which movie is the highest-grossing film of all time",
            "options": ["Avatar", "Avengers: Endgame", "Titanic", "Star Wars: Force Awakens"],
            "correct": "Avatar"
        }
    ]
}

# Save the dictionary as a JSON file
with open('quiz_questions.json', 'w') as json_file:
    json.dump(quiz_data, json_file, indent=4)

print("Quiz questions saved to 'quiz_questions.json'.")
