
original_tuple = ("hello", 10, "goodbye", 3, "goodnight", 5)


user_input = input("Enter a value to append to the tuple: ")


try:
    original_tuple.append(user_input)
except AttributeError:
    
    original_tuple = (*original_tuple, user_input)
    print("Successfully appended value to the tuple using unpacking. Updated tuple:", original_tuple)
