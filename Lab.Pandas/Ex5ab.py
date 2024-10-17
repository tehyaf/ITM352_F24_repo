import pandas as pd
import gdown

url = "https://drive.google.com/uc?export=download&id=1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex"
output = "properties_data.csv"
gdown.download(url, output, quiet=False)

df = pd.read_csv(output)

print(f"Dimensions of the DataFrame: {df.shape}")

print("\nFirst 10 rows of the DataFrame:")
print(df.head(10))

filtered_df = df[df['units'] >= 500]

columns_to_drop = ['address', 'owner'] 
filtered_df = filtered_df.drop(columns=columns_to_drop, errors='ignore')

print("\nFiltered Data (Properties with 500 or more units):")
print(filtered_df.head(10))

print("\nOriginal Data Types:")
print(df.dtypes)

df['units'] = pd.to_numeric(df['units'], errors='coerce')
df['sale price'] = pd.to_numeric(df['sale price'], errors='coerce')
df['date'] = pd.to_datetime(df['date'], errors='coerce') 

print("\nCleaned Data Types:")
print(df.dtypes)

null_values = df[df.isnull().any(axis=1)]
print("\nRows with Null Values:")
print(null_values)

df_cleaned = df.dropna()  
df_cleaned = df_cleaned.drop_duplicates() 

print(f"\nData after dropping null values and duplicates (Rows: {df_cleaned.shape[0]}):")
print(df_cleaned.head(10))

df_filtered_sales = df_cleaned[df_cleaned['Sale Price'] > 0]

print("\nData after filtering out 0 sales:")
print(df_filtered_sales.head(10))

average_price = df_filtered_sales['Sale Price'].mean()
print(f"\nAverage Sales Price: ${average_price:.2f}")