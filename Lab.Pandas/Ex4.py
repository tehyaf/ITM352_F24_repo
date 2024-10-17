import gdown
import pandas as pd

url = "https://drive.google.com/uc?export=download&id=1-MpDUIRZxhFnN-rcDdJQMe_mcCSciaus"
output = "taxi_trip_data.json"
gdown.download(url, output, quiet=False)

df = pd.read_json(output)

print("Summary Statistics:")
print(df.describe())

median_values = df.median()

print("\nMedian Values:")
for column, median_value in median_values.items():
    print(f"{column}: {median_value}")

