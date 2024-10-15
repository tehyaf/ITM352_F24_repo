import json

# Open and read the JSON file
with open('quiz_questions.json', 'r') as json_file:
    quiz_data = json.load(json_file)

# Print the content of the JSON file
print(json.dumps(quiz_data, indent=4))
