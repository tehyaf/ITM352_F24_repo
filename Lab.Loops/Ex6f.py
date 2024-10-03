
original_tuple = ("hello", 10, "goodbye", 3, "goodnight", 5)


user_input = input("Enter a value to append to the tuple: ")


try:
    original_tuple.append(user_input)  
except AttributeError:
  
    temp_list = list(original_tuple)
    temp_list.append(user_input)
    original_tuple = tuple(temp_list)
    print("Successfully appended value to the tuple using .append(). Updated tuple:", original_tuple)
