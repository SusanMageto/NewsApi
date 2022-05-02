import os

'''
import the os module that will allow our application to interact with the operating system dependent functionality.
'''

class Config:

    HEADLINES_API_URL= 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCES_API_URL='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SEARCH_API_URL='https://newsapi.org/v2/everything?q=Apple&from=2022-05-02&sortBy=popularity&apiKey={}'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
