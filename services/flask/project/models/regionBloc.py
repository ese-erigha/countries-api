from mongoengine import DynamicEmbeddedDocument
from mongoengine.fields import StringField, ListField

class RegionBlocModel(DynamicEmbeddedDocument):
    acronym = StringField()
    name = StringField()
    otherAcronyms = ListField(StringField())
    otherNames = ListField(StringField())
