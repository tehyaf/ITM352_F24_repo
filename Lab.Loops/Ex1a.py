odd_numbers_a = []
for num in range(1, 51):
    if num % 2 != 0:  # check if number is odd
        odd_numbers_a.append(num)

print("Odd numbers (traditional for loop with if):", odd_numbers_a)
