from project.models.country import CountryModel


def fetch_countries():
    countries = CountryModel.objects().to_json()
    return countries


def save_country(data):
    country = CountryModel(**data).save()
    return country.to_json()
