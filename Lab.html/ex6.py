import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')  

if not table:
    print("Mortgage rates table not found on the page.")
else:
    headers = [th.get_text(strip=True) for th in table.find_all('th')]

    rows = table.find_all('tr')[1:]  

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == len(headers):
            lender_info = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}
            print(f"Lender: {lender_info.get('Lender', 'N/A')}")
            for header in headers[1:]:  
                print(f"  {header}: {lender_info.get(header, 'N/A')}")
            print()  



