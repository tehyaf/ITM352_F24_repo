import random
import json

def load_questions_from_json(file_path):
    """Load quiz questions from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['questions']

def shuffle_questions(questions):
    """Return a shuffled list of questions."""
    random.shuffle(questions)
    return questions

def display_question(question_data, labels):
    """Display the question and its answer options."""
    question = question_data["question"]
    options = question_data["options"]
    print(f"\n{question}")
    for i, option in enumerate(options):
        print(f"{labels[i]}. {option}")

def get_user_input(labels):
    """Get and validate the user's input."""
    while True:
        user_input = input("\nEnter the letter of your answer: ").upper()
        if user_input in labels:
            return user_input
        else:
            print("Invalid input. Please enter a valid letter (A, B, C, or D).")

def check_answer(selected_answer, correct_answer):
    """Check if the selected answer is correct."""
    if selected_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect! Please try again.")
        return False

def quiz_game():
    """Main function to run the quiz game."""
    score = 0  # Track the number of correct answers
    total_attempts = 0  # Track total attempts by the user
    labels = ['A', 'B', 'C', 'D']  # Labels for answer options

    # Load questions from JSON file
    questions = load_questions_from_json('quiz_questions.json')
    shuffled_questions = shuffle_questions(questions)  # Get shuffled questions

    print("\nWelcome to the Quiz Game!")
    print("-------------------------")
    
    for question_data in shuffled_questions:
        correct_answer = question_data["correct"]
        options = question_data["options"]
        
        random.shuffle(options)  # Shuffle answer options for each question

        # Loop until the user provides the correct answer
        correct = False
        attempts = 0
        
        while not correct:
            display_question(question_data, labels)  # Display the question and options
            user_input = get_user_input(labels)  # Get validated user input
            selected_answer = options[labels.index(user_input)]
            attempts += 1
            total_attempts += 1

            # Check if the answer is correct
            correct = check_answer(selected_answer, correct_answer)

    # Show the final score and number of attempts
    print("\n-------------------------")
    print(f"Quiz Completed! Your final score is: {score}/{len(questions)}")
    print(f"Total attempts: {total_attempts}")
    print("Thank you for playing!")

# Call the game function to run it
quiz_game()








