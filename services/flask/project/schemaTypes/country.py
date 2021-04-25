from promise import Promise
from promise.dataloader import DataLoader
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from project.models.country import CountryModel


class CountryNotFound(graphene.ObjectType):
    message = graphene.String()


class CountryLoader(DataLoader):
    @classmethod
    def batch_load_fn(cls, keys):
        countries = {country.alpha3Code: country for country in CountryModel.objects(alpha3Code__in=keys)}
        return Promise.resolve([countries.get(key) for key in keys])


class Country(MongoengineObjectType):
    class Meta:
        model = CountryModel
        interfaces = (Node,)

    borders = graphene.List(lambda: Country)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.borders = None

    def resolve_borders(self, _info):
        return CountryLoader().load_many(self.borders)


class CountryResponse(graphene.Union):
    class Meta:
        types = (Country, CountryNotFound)
