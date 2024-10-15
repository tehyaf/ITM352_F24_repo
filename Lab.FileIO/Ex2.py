import csv

realinc_sum = 0
realinc_count = 0
realinc_max = float('-inf')
realinc_min = float('inf')

# Open the CSV file
with open('survey_1000.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        try:
            # Get the REALINC value from the 5457th field (index 5456 in 0-based indexing)
            realinc_value = float(row[5456])
            
            # Check if the value is greater than 0
            if realinc_value > 0:
                realinc_sum += realinc_value
                realinc_count += 1
                realinc_max = max(realinc_max, realinc_value)
                realinc_min = min(realinc_min, realinc_value)
        
        except (ValueError, IndexError):
            # Handle cases where the field is non-numeric or missing (ValueError) or the row is too short (IndexError)
            continue

# Calculate the average only if we have valid entries
if realinc_count > 0:
    realinc_avg = realinc_sum / realinc_count
else:
    realinc_avg = 0

# Print the results
print(f"Average REALINC value: {realinc_avg}")
print(f"Maximum REALINC value: {realinc_max}")
print(f"Minimum REALINC value: {realinc_min}")
print(f"Number of REALINC values greater than 0: {realinc_count}")

