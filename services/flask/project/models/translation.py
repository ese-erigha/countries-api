from mongoengine import DynamicEmbeddedDocument
from mongoengine.fields import StringField


class TranslationModel(DynamicEmbeddedDocument):
    br = StringField()
    de = StringField()
    es = StringField()
    fa = StringField()
    fr = StringField()
    hr = StringField()
    it = StringField()
    ja = StringField()
    nl = StringField()
    pt = StringField()
