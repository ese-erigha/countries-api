from mongoengine import Document
from mongoengine.fields import StringField

class TodoModel(Document):
    meta = {'collection': 'todo'}
    todo = StringField(required=True)
