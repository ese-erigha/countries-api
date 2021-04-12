# from mongoengine import Document
import mongoengine_goodjson as gj
from mongoengine.fields import StringField

class TodoModel(gj.Document):
    meta = {'collection': 'todo'}
    todo = StringField(required=True)
