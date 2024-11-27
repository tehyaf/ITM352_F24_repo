import json
import requests
import matplotlib.pyplot as plt

# get json file
url = "https://drive.google.com/uc?id=1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ"
response = requests.get(url)
data = response.json()

print("First row of the JSON file:")
print(data[0]) 

#  Print first 10 rows
print("\nInspecting the first 10 rows of the data:")
for i, trip in enumerate(data[:10]):  
    print(f"Row {i}:")
    print(f"payment_method: {trip.get('payment_method')}")
    print(f"tips: {trip.get('tips')}")

# Filter out rows anything invalid 
filtered_data = []
print("\nFiltering rows:")
for trip in data:
    payment_method = trip.get("payment_method")
    tips = trip.get("tips")
    try:
        tips = float(tips)  
        if payment_method and tips >= 0:
            filtered_data.append({"payment_method": payment_method, "tips": tips})
        else:
            print(f"Skipping invalid row: {trip}")
    except (TypeError, ValueError):
        print(f"Skipping invalid row (non-numeric tips): {trip}")

print(f"\nNumber of valid rows after filtering: {len(filtered_data)}")

# Print the first 5 filtered rows
print("\nFirst 5 rows of filtered data:")
print(filtered_data[:5])

# organize payment method
tips_by_payment_method = {}
for trip in filtered_data:
    payment_method = trip["payment_method"]
    tips = trip["tips"]
    tips_by_payment_method[payment_method] = tips_by_payment_method.get(payment_method, 0) + tips

# Print data
print("\nAggregated tips by payment method:")
print(tips_by_payment_method)

# Create bar chart
if tips_by_payment_method:
    payment_methods = list(tips_by_payment_method.keys())
    sum_of_tips = list(tips_by_payment_method.values())

    plt.bar(payment_methods, sum_of_tips, color="skyblue", edgecolor="black")

    plt.title("Sum of Tips by Payment Method")
    plt.xlabel("Payment Method")
    plt.ylabel("Sum of Tips")

    plt.show()
else:
    print("No valid data to plot. Please check the JSON file or filtering logic.")

