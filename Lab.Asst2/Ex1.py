# Step 1: Import necessary libraries
import pandas as pd
import gdown

# Step 2: Define the URL of the CSV file on Google Drive
url = "https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

# Step 3: Download the file using gdown
gdown.download(url, "full_sales_data.csv", quiet=False)

# Step 4: Read the downloaded file using pandas
data = pd.read_csv("full_sales_data.csv")

# Step 5: Select the first 10 rows
sample_data = data.head(10)

# Step 6: Write the sample data to a new CSV file
sample_data.to_csv("sales_data_test.csv", index=False)

print("Sample data saved as 'sales_data_test.csv' for testing.")
