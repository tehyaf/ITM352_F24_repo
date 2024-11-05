import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410'

dfs = pd.read_html(url)  

interest_rate_df = dfs[0]

print("Columns in the table:", interest_rate_df.columns)

for index, row in interest_rate_df.iterrows():
    if '1 month interest rate' in interest_rate_df.columns:
        print("1 month Interest Rate:", row['1 mo'])
    else:
        print("Column '1 month' not found in table.")
