from project.models.country import CountryModel
from project.models.currency import CurrencyModel
from project.models.language import LanguageModel
from project.models.regionBloc import RegionBlocModel
from project.models.translation import TranslationModel


def map_field_list_to_dict(field_list, data):
    country_dict = {}
    for field in field_list:
        if data[field] is not None:
            country_dict[field] = data[field]

    return country_dict


def map_root_fields(data):
    country_fields_in_root = [
        'alpha2Code', 'alpha3Code', 'area',
        'capital', 'cioc', 'demonym',
        'gini', 'name', 'nativeName',
        'numericCode', 'population', 'region',
        'subregion', 'altSpellings', 'borders',
        'callingCodes', 'latlng', 'timezones',
        'topLevelDomain', 'flag'
    ]

    return map_field_list_to_dict(country_fields_in_root, data)


def map_embedded_field(field_name, field_data):
    model_list = []
    field_list = get_field_list_for_model(field_name)
    field_model = get_model_for_field(field_name)
    for item in field_data:
        mapped_model = map_field_list_to_dict(field_list, item)
        model_list.append(field_model(**mapped_model))
    return model_list


def get_model_for_field(name):
    model_mapping = {
        'currencies': CurrencyModel,
        'languages': LanguageModel,
        'regionalBlocs': RegionBlocModel,
        'translations': TranslationModel
    }
    return model_mapping[name]


def get_field_list_for_model(model_name):
    model_field_mappings = {
        'currencies': ['code', 'name', 'symbol'],
        'languages': ['iso639_1', 'iso639_2', 'name', 'nativeName'],
        'regionalBlocs': ['acronym', 'name', 'otherAcronyms', 'otherNames'],
        'translations': ['br', 'de', 'es', 'fa', 'fr', 'hr', 'it', 'ja', 'nl', 'pt']
    }
    return model_field_mappings.get(model_name)


def fetch_countries():
    countries = CountryModel.objects().to_json()
    return countries


def save_country(data):
    root_fields = map_root_fields(data)
    country = CountryModel(**root_fields)

    mapping_fields = ['currencies', 'languages', 'regionalBlocs']
    for field in mapping_fields:
        country[field] = map_embedded_field(
            field,
            data[field],
        )
    country.translations = TranslationModel(**data['translations'])
    country_item = country.save()
    return country_item.to_json()
