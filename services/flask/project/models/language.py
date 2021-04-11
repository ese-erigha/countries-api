from mongoengine import DynamicEmbeddedDocument
from mongoengine.fields import StringField

class LanguageModel(DynamicEmbeddedDocument):
    iso639_1 = StringField()
    iso639_2 = StringField()
    name = StringField()
    nativeName = StringField()
