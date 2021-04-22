import graphene
from graphene.relay import Node
from project.models.country import CountryModel
from project.schemaTypes.country import Country
from project.dto.country import MappedCountry
from project.elasticSearch.country import CountrySearch


class CountryInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    region = graphene.String(required=False)
    offset = graphene.Int(required=False, default_value=0)


class Query(graphene.ObjectType):
    node = Node.Field()
    countries = graphene.List(MappedCountry, countryInput=CountryInput(required=True))
    country = graphene.Field(Country, id=graphene.String(required=True))

    @staticmethod
    def resolve_countries(_, _info, countryInput):
        return CountrySearch().search(countryInput)

    @staticmethod
    def resolve_country(_, _info, id):
        return CountryModel.objects().get(id=id)


schema = graphene.Schema(query=Query, types=[MappedCountry, Country])
