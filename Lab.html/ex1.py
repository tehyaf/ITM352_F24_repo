import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data'

response = urllib.request.urlopen(url)
print("Response Object:", response)

html_content = response.readlines()
for line in html_content:
    decoded_line = line.decode('utf-8')
    if '<title>' in decoded_line:
        print("Title Line:", decoded_line)