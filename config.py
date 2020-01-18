from decouple import config as env_conf


class Config(object):
    DEBUG = False
    POSTGRES_USER = env_conf('POSTGRES_USER')
    POSTGRES_PW = env_conf('POSTGRES_PWD')
    POSTGRES_HOST = env_conf('POSTGRES_HOST')
    POSTGRES_DB = env_conf('POSTGRES_DATABASE')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pw}@{host}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PW, host=POSTGRES_HOST, db=POSTGRES_DB)
