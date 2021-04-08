from project import db
from .currency import Currency
from .language import Language
from .regionBloc import RegionBloc
from .translation  import Translation

class Country(db.Document):
    alpha2Code = db.StringField(required=True, unique=True)
    alpha3Code = db.StringField(required=True, unique=True)
    altSpellings = db.ListField(db.StringField())
    area = db.IntField()
    borders = db.ListField(db.StringField())
    callingCodes = db.ListField(db.StringField())
    capital = db.StringField(required=True)
    cioc = db.StringField()
    currencies = db.EmbeddedDocumentListField(Currency)
    demonym = db.StringField()
    flag = db.StringField()
    gini = db.FloatField()
    languages = db.EmbeddedDocumentListField(Language)
    latlng = db.ListField(db.DecimalField())
    name = db.StringField()
    nativeName = db.StringField()
    numericCode = db.StringField()
    population = db.DecimalField()
    region = db.StringField()
    regionalBlocs = db.EmbeddedDocumentListField(RegionBloc)
    subregion = db.StringField()
    timezones = db.ListField(db.StringField())
    topLevelDomain = db.ListField(db.StringField())
    translations = db.EmbeddedDocumentListField(Translation)