import requests
from bs4 import BeautifulSoup

url = 'https://shidler.hawaii.edu/itm/people'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.prettify()[:500])  
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

faculty_sections = soup.find_all('div', class_='views-row')

faculty_names = []

for section in faculty_sections:
    header = section.find('h2')
    if header:
        name = header.get_text(strip=True)
        faculty_names.append(name)

for name in faculty_names:
    print(name)

print(f"Total number of faculty members found: {len(faculty_names)}")
