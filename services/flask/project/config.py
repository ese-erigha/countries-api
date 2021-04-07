import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MONGO_URI =  'mongodb://' + os.getenv('MONGODB_USERNAME','') + ':' + os.getenv('MONGODB_PASSWORD','') + '@' + os.getenv('MONGODB_HOSTNAME','') + ':27017/' + os.getenv('MONGODB_DATABASE','')
