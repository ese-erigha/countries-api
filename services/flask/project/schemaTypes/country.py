from promise import Promise
from promise.dataloader import DataLoader
import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from project.models.country import CountryModel


class CountryLoader(DataLoader):
    @classmethod
    def batch_load_fn(cls, keys):
        countries = {country.alpha2Code: country for country in CountryModel.objects(alpha2Code__in=keys)}
        return Promise.resolve([countries.get(key) for key in keys])


class Country(MongoengineObjectType):
    class Meta:
        model = CountryModel
        interfaces = (Node,)

    border_countries = graphene.List(lambda: Country)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.borders = None

    def resolve_border_countries(self):
        return CountryLoader().load_many(self.borders)
