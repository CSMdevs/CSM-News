import requests
import json

# The JSON
contents = requests.get("https://newsapi.org/v2/top-headlines?country=nl&apiKey=4898a7ecddb347c8b3998f1146d7b7a9").json()

status = contents['status']
totalResults = contents['totalResults']
source1 = contents['articles'][0]['source']['name']

print(status)
print(totalResults)
print(source1)

def my_function(contents):
    for x in contents['articles']:
        print("Source: " + str(x['source']['name']))
        print("Author: " + str(x['author']))
        print("Title: " + str(x['title']))
        print("Description: " + str(x['description']))
        print("Url: " + str(x['url']))
        print("Url: " + str(x['url']))

my_function(contents)