import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')




class TestConfig(Config):


    pass
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    DEBUG= True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'


config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}