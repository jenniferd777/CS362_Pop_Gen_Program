import requests
import json

# variables

response = requests.get('https://api.census.gov/data/2019/acs/acs1/spp?get=NAME,S0201_001E&for=state:*')
for data in response.json()['items']:
    print(data['title'])



