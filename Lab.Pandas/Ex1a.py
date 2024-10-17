import numpy as np

data = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292)
]

data_array = np.array(data)

dimensions = data_array.shape
num_elements = data_array.size

print(f"Dimensions of the array: {dimensions}")
print(f"Number of elements: {num_elements}")

print("\nTable of Percentiles and Household Incomes:")
print("Percentile    Income")
for percentile, income in data:
    print(f"{percentile:<12} {income}")
