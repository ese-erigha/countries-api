from mongoengine import DynamicEmbeddedDocument
from mongoengine.fields import StringField


class CurrencyModel(DynamicEmbeddedDocument):
    code = StringField(required=True)
    name = StringField(required=True)
    symbol = StringField()
