from urllib import parse 


class Config:
    SECRET_KEY = 'secrets'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_CXN = 'Driver=...'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
