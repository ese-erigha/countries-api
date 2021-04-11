from promise import Promise
from promise.dataloader import DataLoader
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from project.models.country import CountryModel

class CountryLoader(DataLoader):

    def batch_load_fn(self, keys):
        countries = {country.alpha2Code: country for country in CountryModel.objects(alpha2Code__in=keys)}
        return Promise.resolve([countries.get(key) for key in keys])

class Country(MongoengineObjectType):

    class Meta:
        model = CountryModel
        interfaces = (Node,)

    border_countries = graphene.List(lambda: Country)

    def resolve_border_countries(root, info):
        return CountryLoader().load_many(root.borders)

    