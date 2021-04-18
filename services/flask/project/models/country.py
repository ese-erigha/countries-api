from mongoengine.fields import StringField, ListField, EmbeddedDocumentListField, \
    EmbeddedDocumentField, IntField, DecimalField, FloatField
import mongoengine_goodjson as gj
from .currency import CurrencyModel
from .language import LanguageModel
from .regionBloc import RegionBlocModel
from .translation import TranslationModel


class CountryModel(gj.Document):
    meta = {'collection': 'country'}
    alpha2Code = StringField(required=True, unique=True)
    alpha3Code = StringField()
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
    translations = EmbeddedDocumentField(TranslationModel)
