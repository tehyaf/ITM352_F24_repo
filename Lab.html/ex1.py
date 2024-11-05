import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data'

response = urllib.request.urlopen(url)
print("Response Object:", response)

