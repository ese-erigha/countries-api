from project import db

class RegionBloc(db.DynamicEmbeddedDocument):
    acronym = db.StringField()
    name = db.StringField()
    otherAcronyms = db.ListField(db.StringField())
    otherNames = db.ListField(db.StringField())
