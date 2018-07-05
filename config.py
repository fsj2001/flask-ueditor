# -*- coding: utf-8 -*-
class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    PORT = 5001
    HOST = '0.0.0.0'
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:kbsonlong@blog_db:8080/blog'