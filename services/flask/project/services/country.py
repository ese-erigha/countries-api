from project.models.country import CountryModel

def fetchCountries():
    countries = CountryModel.objects().to_json()
    return countries

def addCountry(data):
    CountryModel(**data).save()
