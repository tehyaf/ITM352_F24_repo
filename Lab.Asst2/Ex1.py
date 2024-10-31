import pandas as pd
import gdown

url = "https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

gdown.download(url, "full_sales_data.csv", quiet=False)

data = pd.read_csv("full_sales_data.csv")

sample_data = data.head(10)

sample_data.to_csv("sales_data_test.csv", index=False)

print("Sample data saved as 'sales_data_test.csv' for testing.")
