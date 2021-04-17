from mongoengine import DynamicEmbeddedDocument
from mongoengine.fields import StringField


class CurrencyModel(DynamicEmbeddedDocument):
    code = StringField()
    name = StringField()
    symbol = StringField()
