import os

'''
import the os module that will allow our application to interact with the operating system dependent functionality.
'''

class Config:
    """
    General configuration parent class
    """
    HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SOURCE_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY= "1663536f3bec419493c8319198a2c47a"

class ProdConfig(Config):
    """
    Production  configuration child class

    Args:Config: The parent configuration class with General configuration settings
    """
    pass


class DevConfig(Config):
    """
    Development  configuration child class

    Args:Config: The parent configuration class with General configuration settings
    """
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
