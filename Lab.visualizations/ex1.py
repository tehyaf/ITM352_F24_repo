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

# get trip miles data
trip_miles = [trip["trip_miles"] for trip in data if "trip_miles" in trip]

# Create histogram
plt.hist(trip_miles, bins=20, edgecolor="black", color="blue")

# for title and axis labels
plt.title("Histogram of Trip Miles")
plt.xlabel("Trip Miles")
plt.ylabel("Frequency")

# Show the plot
plt.show()

