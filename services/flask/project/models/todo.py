from project import db

class Todo(db.Document):
    todo = db.StringField(required=True)
