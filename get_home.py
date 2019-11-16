import urllib.request
import json

# The JSON
contents = urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=nl&apiKey=4898a7ecddb347c8b3998f1146d7b7a9").read()

