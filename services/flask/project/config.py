import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    MONGODB_SETTINGS = {
        'host':'mongodb://localhost/'+ os.getenv('MONGODB_DATABASE','')
    }
    
