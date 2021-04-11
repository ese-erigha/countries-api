from mongoengine import Document
from mongoengine.fields import StringField, ListField, EmbeddedDocumentListField, IntField, DecimalField, FloatField
from .currency import CurrencyModel
from .language import LanguageModel
from .regionBloc import RegionBlocModel
from .translation  import TranslationModel

class CountryModel(Document):
    meta = {'collection': 'country'}
    alpha2Code = StringField(required=True, unique=True)
    alpha3Code = StringField(required=True, unique=True)
    altSpellings = ListField(StringField())
    area = IntField()
    borders = ListField(StringField())
    callingCodes = ListField(StringField())
    capital = StringField(required=True)
    cioc = StringField()
    currencies = EmbeddedDocumentListField(CurrencyModel)
    demonym = StringField()
    flag = StringField()
    gini = FloatField()
    languages = EmbeddedDocumentListField(LanguageModel)
    latlng = ListField(DecimalField())
    name = StringField()
    nativeName = StringField()
    numericCode = StringField()
    population = DecimalField()
    region = StringField()
    regionalBlocs = EmbeddedDocumentListField(RegionBlocModel)
    subregion = StringField()
    timezones = ListField(StringField())
    topLevelDomain = ListField(StringField())
    translations = EmbeddedDocumentListField(TranslationModel)