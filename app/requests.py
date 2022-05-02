import urllib.request,json


from .models import sources
from .models import articles


# Getting api key
api_key = None
# Getting the news base url
sources_url = None
headlines_url=None
search_url=None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    sources_url=app.config['SOURCES_API_URL']
    headlines_url=app.config['HEADLINES_API_URL']
    search_url=app.config['SEARCH_API_URL']
    