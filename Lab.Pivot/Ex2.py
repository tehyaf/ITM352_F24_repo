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

    sales_data['sales'] = sales_data['quantity'] * sales_data['unit_price']

    print("\nFirst 5 rows with 'sales' column:")
    print(sales_data.head())

    sales_pivot = sales_data.pivot_table(
        values='sales',  
        index='sales_region',  
        columns='order_type',  
        aggfunc='sum',  
        fill_value=0  
    )

    print("\nPivot Table - Sales by Region and Order Type:")
    print(sales_pivot)

except Exception as e:
    print(f"An error occurred while reading the file: {e}")
