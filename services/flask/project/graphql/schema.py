import elasticsearch
import graphene
import mongoengine
from graphene.relay import Node
from project.models.country import CountryModel
from project.schemaTypes.country import CountryResponse, CountryNotFound
from project.dto.country import CountrySearchResponse, CountrySearchError
from project.elasticSearch.country import CountrySearch


class CountryInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    region = graphene.String(required=False)
    offset = graphene.Int(required=False, default_value=0)


class Query(graphene.ObjectType):
    node = Node.Field()
    countries = graphene.Field(CountrySearchResponse, countryInput=CountryInput(required=True))
    country = graphene.Field(CountryResponse, id=graphene.String(required=True))

    @staticmethod
    def resolve_countries(_, _info, countryInput):
        try:
            return CountrySearch().search(countryInput)
        except elasticsearch.ElasticsearchException as err:
            return CountrySearchError(message=str(err))

    @staticmethod
    def resolve_country(_, _info, id):
        try:
            return CountryModel.objects().get(metaId=id)
        except mongoengine.DoesNotExist:
            return CountryNotFound(message="Item not found")


schema = graphene.Schema(query=Query, types=[CountrySearchResponse, CountryResponse])
