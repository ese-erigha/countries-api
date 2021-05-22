from os import path, getenv
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

mode = getenv("MODE")
if mode == "local":
    load_dotenv(path.join(basedir, '.env.local'))


class Config(object):
    DEBUG = True
    DB_NAME = getenv("MONGO_INITDB_DATABASE")
    DB_HOST = getenv("MONGO_HOST")
    DB_PORT = getenv("MONGO_PORT")
    ELASTICSEARCH_HOST = getenv("ELASTICSEARCH_HOST")
    DB_USERNAME = getenv("MONGO_INITDB_ROOT_USERNAME")
    DB_PASSWORD = getenv("MONGO_INITDB_ROOT_PASSWORD")
    AUTH_TOKEN = getenv("AUTH_TOKEN")


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    ELASTIC_USERNAME = getenv("ELASTIC_USERNAME")
    ELASTIC_PASSWORD = getenv("ELASTIC_PASSWORD")


class LocalConfig(Config):
    pass
