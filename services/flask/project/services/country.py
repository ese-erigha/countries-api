from project.models.country import Country

def fetchCountries():
    countries = Country.objects().to_json()
    return countries

def addCountry(data):
    Country(**data).save()
