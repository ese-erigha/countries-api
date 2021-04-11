import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField
from project.schemaTypes.country import Country
from project.schemaTypes.todo    import Todo
from .mutations.todo import CreateTodoMutation

class Query(graphene.ObjectType):
    node = Node.Field()
    countries = MongoengineConnectionField(Country)
    todos = MongoengineConnectionField(Todo)

class Mutation(graphene.ObjectType):
    createTodo = CreateTodoMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Country, Todo])