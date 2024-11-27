import json
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Get JSON file 
url = "https://drive.google.com/uc?id=1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python list/dict
else:
    raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

# structure json data
print("First row of the JSON data:")
print(data[0])

# Step 2: Filter by fares, trip miles, and dropoff place
filtered_data = []
for trip in data:
    try:
        fare = float(trip.get("fare", 0))
        trip_miles = float(trip.get("trip_miles", 0))
        dropoff_area = int(trip.get("dropoff_community_area", -1))  # Use -1 for missing areas
        if trip_miles > 0:  # Filter out trips with 0 miles
            filtered_data.append((fare, trip_miles, dropoff_area))
    except (TypeError, ValueError):
        continue  

# Isolate data to be first 5 rows
print("\nFirst 5 rows of filtered data (fare, trip_miles, dropoff_area):")
print(filtered_data[:5])

# Plotting data
fares = [row[0] for row in filtered_data]
trip_miles = [row[1] for row in filtered_data]
dropoff_areas = [row[2] for row in filtered_data]

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
scatter = ax.scatter(fares, trip_miles, dropoff_areas, c=dropoff_areas, cmap="viridis", s=50, alpha=0.8)

#title and axis labels
ax.set_title("3D Plot of Fares, Trip Miles, and Dropoff Area")
ax.set_xlabel("Fare ($)")
ax.set_ylabel("Trip Miles")
ax.set_zlabel("Dropoff Area")

# dropoff area
cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label("Dropoff Area")

# Show the plot
plt.show()
