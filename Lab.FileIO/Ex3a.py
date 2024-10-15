import csv

# Initialize variables to store calculations
total_fares = 0
total_trips = 0
max_trip_distance = float('-inf')

# Open the taxi_1000.csv file
with open('taxi_1000.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header (assuming the file has one)
    next(csv_reader)
    
    for row in csv_reader:
        try:
            # Read the Fare and Trip Miles fields (assuming Fare is at index 8 and Trip Miles is at index 5)
            fare = float(row[8])
            trip_miles = float(row[5])
            
            # Add to the total fares and increment trip count
            total_fares += fare
            total_trips += 1
            
            # Update the maximum trip distance
            if trip_miles > max_trip_distance:
                max_trip_distance = trip_miles
                
        except (ValueError, IndexError):
            # Handle rows with invalid data or missing fields
            continue

# Calculate the average fare
if total_trips > 0:
    average_fare = total_fares / total_trips
else:
    average_fare = 0

# Print the results
print(f"Total of all fares: ${total_fares:.2f}")
print(f"Average fare: ${average_fare:.2f}")
print(f"Maximum trip distance: {max_trip_distance:.2f} miles")
