import gdown
import csv

# Google Drive file ID
file_id = '10X2Icx78XKTbt3ZRj3F-FlzmW_NugEpz'
# Convert to a downloadable link
download_url = f'https://drive.google.com/uc?id={file_id}'

# Output filename for the downloaded file
output_file = 'taxi_1000.csv'

# Step 1: Download the file from Google Drive
gdown.download(download_url, output_file, quiet=False)

# Step 2: Initialize variables to store calculations
total_fares = 0
total_trips = 0
max_trip_distance = float('-inf')

# Step 3: Open the taxi_1000.csv file
with open(output_file, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header (assuming the file has one)
    next(csv_reader)
    
    for row in csv_reader:
        try:
            # Read the Fare and Trip Miles fields (assuming Fare is at index 8 and Trip Miles is at index 5)
            fare = float(row[8])
            trip_miles = float(row[5])
            
            # Only process records where fare is greater than $10
            if fare > 10:
                # Add to the total fares and increment trip count
                total_fares += fare
                total_trips += 1

                # Update the maximum trip distance
                if trip_miles > max_trip_distance:
                    max_trip_distance = trip_miles
                
        except (ValueError, IndexError):
            # Handle rows with invalid data or missing fields
            continue

# Step 4: Calculate the average fare
if total_trips > 0:
    average_fare = total_fares / total_trips
else:
    average_fare = 0

# Step 5: Print the results
print(f"Total of all fares greater than $10: ${total_fares:.2f}")
print(f"Average fare for trips greater than $10: ${average_fare:.2f}")
print(f"Maximum trip distance for trips with fares greater than $10: {max_trip_distance:.2f} miles")
