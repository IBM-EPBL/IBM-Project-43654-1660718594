class Config:
    
    NEWS_BASE_URL_SOURCES = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=7e535c4ed1044f4ab17b70d0efd2a84b'
    NEWS_BASE_EVERYTHING_URL = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=7e535c4ed1044f4ab17b70d0efd2a84b'
    NEWS_BASE_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=7e535c4ed1044f4ab17b70d0efd2a84b'
    NEWS_BASE_SOURCE = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=7e535c4ed1044f4ab17b70d0efd2a84b'
    API_KEY = "7e535c4ed1044f4ab17b70d0efd2a84b"

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options= {
    'development': DevConfig,
    'production': ProdConfig
}