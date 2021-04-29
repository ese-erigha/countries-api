from os import path, getenv
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

mode = getenv("MODE")
if mode == "local":
    load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DB_NAME = getenv("MONGO_INITDB_DATABASE")
    DB_HOST = getenv("MONGO_HOST")
    DB_PORT = getenv("MONGO_PORT")
    ELASTICSEARCH_HOST = getenv("ELASTICSEARCH_HOST")


class ProductionConfig(Config):
    DEBUG = False
    DB_USERNAME = getenv("DATABASE_USERNAME")
    DB_PASSWORD = getenv("DATABASE_PASSWORD")


class DevelopmentConfig(Config):
    DEBUG = True


class LocalConfig(Config):
    DEBUG = True
