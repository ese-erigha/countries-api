import graphene
from graphene.relay import Node
from project.models.country import CountryModel
from project.schemaTypes.country import Country
from project.dto.country import MappedCountry
from project.graphql.mutations.todo import CreateTodoMutation
from project.elasticSearch.country import CountrySearch


class Query(graphene.ObjectType):
    node = Node.Field()
    countries_in_region = graphene.List(MappedCountry,
                                        region=graphene.String(),
                                        offset=graphene.Int()
                                        )
    countries_by_name = graphene.List(MappedCountry,
                                      name=graphene.String(),
                                      offset=graphene.Int()
                                      )
    country = graphene.Field(Country, id=graphene.String(required=True))

    @staticmethod
    def resolve_countries_in_region(_, _info, region, offset):
        return CountrySearch().search_by_region(region, offset)

    @staticmethod
    def resolve_countries_by_name(_, _info, name, offset):
        return CountrySearch().search_by_name(name, offset)

    @staticmethod
    def resolve_country(_, _info, id):
        return CountryModel.objects().get(id=id)


class Mutation(graphene.ObjectType):
    createTodo = CreateTodoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[MappedCountry, Country])
