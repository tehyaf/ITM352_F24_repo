# Original tuple
original_tuple = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Get input from the user
user_input = input("Enter a value to append to the tuple: ")

# Try to append the value using the unpacking operator
try:
    original_tuple.append(user_input)
except AttributeError:
    # Use unpacking operator to create a new tuple
    original_tuple = (*original_tuple, user_input)
    print("Successfully appended value to the tuple using unpacking. Updated tuple:", original_tuple)
