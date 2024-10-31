import pandas as pd
import time

def load_csv(file_path):
    """
    Loads a CSV file into a DataFrame with pyarrow backend, skipping bad rows.
    Checks for required columns and prints information about the DataFrame.
    """
    required_columns = ["quantity", "unit_price"]
    start_time = time.time()
    
    print(f"Loading file: {file_path} ...")
    try:
        data = pd.read_csv(file_path, engine="pyarrow", on_bad_lines="skip", parse_dates=True)
        
        load_time = time.time() - start_time
        print(f"File loaded successfully in {load_time:.2f} seconds.")
        
        print(f"Number of rows: {len(data)}")
        print("Columns:", list(data.columns))
        
        for col in data.select_dtypes(include=["datetime"]):
            data[col] = data[col].dt.strftime("%Y-%m-%d")
        
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Warning: Missing columns {missing_columns}. Some analytics may not function properly.")
        
        return data
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.ParserError:
        print("Error: error encountered while loading the CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

test_data = load_csv("sales_data_test.csv")
drive_data = load_csv("full_sales_data.csv") 
