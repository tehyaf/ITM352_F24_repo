import json
import requests
import matplotlib.pyplot as plt

# get json file
url = "https://drive.google.com/uc?id=1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  
else:
    raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

# get fares and trip miles
fares = []
trip_miles = []

for trip in data:
    fare = trip.get("fare")
    miles = trip.get("trip_miles")
    try:
        # Conversion for fare and miles
        fare = float(fare)
        miles = float(miles)
        # more filters 
        if fare >= 0 and miles >= 0:
            fares.append(fare)
            trip_miles.append(miles)
    except (TypeError, ValueError):
        
        print(f"Skipping invalid row: {trip}")

# Print only the first 10 pairs of fares and trip miles
print("\nFirst 10 fare and trip mile pairs:")
for i in range(min(10, len(fares))):
    print(f"Fare: {fares[i]}, Trip Miles: {trip_miles[i]}")

# 4a
plt.scatter(fares, trip_miles, color="blue", alpha=0.5, edgecolor="black")
plt.title("Scatter Plot of Fares vs Trip Miles (plt.scatter)")
plt.xlabel("Fare ($)")
plt.ylabel("Trip Miles")
plt.show()

# 4b
plt.plot(fares, trip_miles, linestyle="none", marker=".", color="green", alpha=0.5)
plt.title("Scatter Plot of Fares vs Trip Miles (plt.plot)")
plt.xlabel("Fare ($)")
plt.ylabel("Trip Miles")
plt.show()

# 4c
plt.scatter(fares, trip_miles, marker="v", color="cyan", alpha=0.2, edgecolor="black")
plt.title("Scatter Plot of Fares vs Trip Miles (Fancy Styling)")
plt.xlabel("Fare ($)")
plt.ylabel("Trip Miles")
plt.show()

