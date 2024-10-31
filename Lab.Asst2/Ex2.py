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
        # Load CSV with pyarrow, skip bad rows, and parse dates automatically
        data = pd.read_csv(file_path, engine="pyarrow", on_bad_lines="skip", parse_dates=True)
        
        # Calculate and print load time
        load_time = time.time() - start_time
        print(f"File loaded successfully in {load_time:.2f} seconds.")
        
        # Print number of rows and list of columns
        print(f"Number of rows: {len(data)}")
        print("Columns:", list(data.columns))
        
        # Format date columns to a more useful format (e.g., YYYY-MM-DD)
        for col in data.select_dtypes(include=["datetime"]):
            data[col] = data[col].dt.strftime("%Y-%m-%d")
        
        # Check for required columns
        missing_columns = [col for col in required_columns if col not in data.columns]
        if missing_columns:
            print(f"Warning: Missing columns {missing_columns}. Some analytics may not function properly.")
        
        return data
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.ParserError:
        print("Error: Parsing error encountered while loading the CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the function with the test file and the Google Drive file
test_data = load_csv("sales_data_test.csv")
drive_data = load_csv("full_sales_data.csv")  # Use the actual file path here if you re-downloaded it
