import requests
import json

# The JSON
contents = requests.get("https://newsapi.org/v2/top-headlines?country=nl&apiKey=4898a7ecddb347c8b3998f1146d7b7a9").json()

status = contents['status']
totalResults = contents['totalResults']
source1 = contents['source']

print('API status: ' + status)
print('Total results: ' + str(totalResults))
print(source1)