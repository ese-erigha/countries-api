from project import db

class Translation(db.DynamicEmbeddedDocument):
    br = db.StringField()
    de = db.StringField()
    es = db.StringField()
    fa = db.StringField()
    fr = db.StringField()
    hr = db.StringField()
    it = db.StringField()
    ja = db.StringField()
    nl = db.StringField()
    pt = db.StringField()
