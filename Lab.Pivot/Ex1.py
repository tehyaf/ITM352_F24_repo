import pandas as pd

csv_url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

try:
    sales_data = pd.read_csv(
        csv_url, 
        dtype_backend='pyarrow',  
        on_bad_lines='skip' 
    )

    sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], errors='coerce')

    print("First 5 rows after converting 'order_date':")
    print(sales_data.head())

    pd.set_option('display.max_columns', None)

    print("\nDisplaying all columns:")
    print(sales_data.head())

except Exception as e:
    print(f"An error occurred while reading the file: {e}")









