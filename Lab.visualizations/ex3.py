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

# chekcing structure 
print("First row of the JSON file:")
print(data[0])  

#  get fares and tips
fares = []
tips = []

for trip in data:
    fare = trip.get("fare")
    tip = trip.get("tips")
    try:
      
        fare = float(fare)
        tip = float(tip)
        # filters for only valid values
        if fare >= 0 and tip >= 0:
            fares.append(fare)
            tips.append(tip)
    except (TypeError, ValueError):
        print(f"Skipping invalid row: {trip}")

# Print the first 10 pairs of fares and tips
print("\nFirst 10 fare and tip pairs:")
for i in range(min(10, len(fares))):
    print(f"Fare: {fares[i]}, Tip: {tips[i]}")

# Create the scatter plot
if fares and tips:
    plt.scatter(fares, tips, color="blue", alpha=0.5, edgecolor="black")

    plt.title("Scatter Plot of Fares vs Tips")
    plt.xlabel("Fare ($)")
    plt.ylabel("Tip ($)")

    plt.show()

