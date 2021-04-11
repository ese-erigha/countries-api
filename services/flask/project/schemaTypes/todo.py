from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from project.models.todo   import TodoModel


class Todo(MongoengineObjectType):

    class Meta:
        model = TodoModel
        interfaces = (Node,)