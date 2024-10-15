with open("names.txt", "a") as file:
    file.write("\nPort, Dan") 

with open("names.txt", "r") as file:
    contents = file.read()

print("Contents of the file after appending:")
print(contents)
