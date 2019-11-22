import requests
import json

# The JSON
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='4898a7ecddb347c8b3998f1146d7b7a9')

# /v2/top-headlines
def function(q=None, sources=None, category=None, language=None, country=None):
    top_headlines = newsapi.get_top_headlines(category=category,
                                          country=country,                                      
                                          domains=domains,
                                          from_param=from_param,
                                          language=language,
                                          page=2,
                                          q=q,
                                          sort_by=sort_by
                                          sources=sources,
                                          to=to)
    return top_headlines

print(function(q='bitcoin'))