even_numbers = [0] 

while even_numbers[-1] < 50: 
    even_numbers.append(even_numbers[-1] + 2)  


even_numbers.pop(0)

print("Even numbers (using last element check):", even_numbers)
