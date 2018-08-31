import os

class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}