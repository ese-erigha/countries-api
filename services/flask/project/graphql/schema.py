import graphene
from graphene.relay import Node
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

    @staticmethod
    def resolve_countries_in_region(_, _info, region, offset):
        return CountrySearch().search_by_region(region, offset)


class Mutation(graphene.ObjectType):
    createTodo = CreateTodoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[MappedCountry, Country])
