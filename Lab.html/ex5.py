import requests
import pandas as pd

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

response = requests.get(url)
data = response.json()  
print("Response JSON data:")
print(data)

df = pd.DataFrame(data)

df = df.rename(columns={'count_license': 'count', 'driver_type': 'driver_type'})
df['count'] = df['count'].astype(int) 

df.set_index('driver_type', inplace=True)

print("\nDataFrame with count by driver_type:")
print(df)
