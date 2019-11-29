import requests
import json
import datetime

# The JSON
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='4898a7ecddb347c8b3998f1146d7b7a9')

# /v2/top-headlines
def function(category=None, country=None, domains=None, from_param=datetime.date(2019, 11, 21), language=None, page=None, pageSize=None, q=None, sort_by=None, sources=None, to=None):
    top_headlines = newsapi.get_top_headlines(category=category,
                                          country=country,
                                          from_param=from_param,
                                          language=language,
                                          page=page,
                                          pageSize=pageSize,
                                          q=q,
                                          sort_by=sort_by,
                                          sources=sources,
                                          to=to)
    return top_headlines

print(function())