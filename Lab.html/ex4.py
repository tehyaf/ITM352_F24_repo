from sodapy import Socrata
import pandas as pd

client = Socrata("data.cityofchicago.org", None)  

data = client.get("rr23-ymwb", limit=500)

df = pd.DataFrame.from_records(data)
print("Column names in the DataFrame:")
print(df.columns)  
print("First few rows of the DataFrame:")
print(df.head())

try:
    print("\nFuel Sources:")
    print(df['vehicle_fuel_source']) 
except KeyError:
    print("\nCould not find the 'vehicle_fuel_source' column. Please verify column name.")

try:
    fuel_counts = df['vehicle_fuel_source'].value_counts()  
    print("\nNumber of vehicles per fuel source:")
    print(fuel_counts)
except KeyError:
    print("\nCounting by 'vehicle_fuel_source' failed. Please check the column name.")




