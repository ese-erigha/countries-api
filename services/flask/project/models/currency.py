from project import db

class Currency(db.DynamicEmbeddedDocument):
    code = db.StringField(required=True)
    name = db.StringField(required=True)
    symbol = db.StringField()
