from project import db

class Language(db.DynamicEmbeddedDocument):
    iso639_1 = db.StringField()
    iso639_2 = db.StringField()
    name = db.StringField()
    nativeName = db.StringField()
