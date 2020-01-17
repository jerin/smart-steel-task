import os
from decouple import config as env_conf

class Config(object):
    DEBUG = False   
    SQLALCHEMY_DATABASE_URI = env_conf('DATABASE_URL1')