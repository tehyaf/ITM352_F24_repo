
original_tuple = ("hello", 10, "goodbye", 3, "goodnight", 5)

user_input = input("Enter a value to append to the tuple: ")


updated_list = list(original_tuple)  
updated_list.append(user_input)      

updated_tuple = tuple(updated_list)

print("Updated tuple:", updated_tuple)
