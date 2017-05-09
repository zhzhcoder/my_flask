import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    @staticmethod
    def init_app(app):
        pass 

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'default' : DevelopmentConfig,
    }
