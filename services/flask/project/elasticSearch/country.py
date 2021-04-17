from elasticsearch_dsl import Document, Long, Keyword, Text, Index

countryIndex = Index('country')


@countryIndex.document
class CountryESModel(Document):
    name = Text(fields={'raw': Keyword()})
    alpha2Code = Keyword()
    capital = Text()
    population = Long()
    region = Keyword()


def init():
    # delete the index, ignore if it doesn't exist
    countryIndex.delete(ignore=404)

    # if countryIndex.exists() is True:

    #     countryIndex.delete()

    countryIndex.settings(number_of_shards=1)
    countryIndex.create()


def index_country(data):
    CountryESModel(
        meta={'id': data['id']},
        name=data['name'],
        alpha2Code=data['alpha2Code'],
        capital=data['capital'],
        population=data['population'],
        region=data['region']
    ).save()

    # refresh index manually to make changes live
    countryIndex.refresh()
