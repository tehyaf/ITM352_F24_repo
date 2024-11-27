import matplotlib.pyplot as plt

# First 
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# Second 
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

# Plot the first set 
plt.plot(x1, y1, label="Line 1")
plt.scatter(x1, y1, color='red', label="Points 1")

# Plot the second set 
plt.plot(x2, y2, label="Line 2")

#  label for graph
plt.title("Line and Scatter Plot Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend() 


plt.show()

