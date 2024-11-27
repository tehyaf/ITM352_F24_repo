import json
import requests
import matplotlib.pyplot as plt

# get json file 
url = "https://drive.google.com/uc?id=1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert to dict/list
else:
    raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

# Filter out trips with 0 or less than 2 miles
filtered_data = []
fares = []
trip_miles = []

for trip in data:
    fare = trip.get("fare")
    miles = trip.get("trip_miles")
    try:
        # Converts fare and trip miles to numbers 
        fare = float(fare)
        miles = float(miles)
        # Filter trips with 0 or less than 2 miles
        if miles > 0 and miles >= 2:
            fares.append(fare)
            trip_miles.append(miles)
    except (TypeError, ValueError):
        # remove rows with invalid data
        print(f"Skipping invalid row: {trip}")

# Print the first 10 pairs
print("\nFirst 10 valid fare and trip mile pairs:")
for i in range(min(10, len(fares))):
    print(f"Fare: {fares[i]}, Trip Miles: {trip_miles[i]}")

# Create scatter plot
plt.scatter(fares, trip_miles, color="blue", alpha=0.5, edgecolor="black")
plt.title("Scatter Plot of Fares vs Trip Miles")
plt.xlabel("Fare ($)")
plt.ylabel("Trip Miles")
plt.savefig("FaresXmiles.png")  # Save the plot to png
plt.show()

