# Original tuple
original_tuple = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Get input from the user
user_input = input("Enter a value to append to the tuple: ")

# Try to append the value to the tuple (which will fail)
try:
    original_tuple.append(user_input)
except AttributeError as e:
    print(f"Error: Attempted to append to the tuple. Reason: {e}")

