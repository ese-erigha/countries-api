import graphene
from project.schemaTypes.todo    import Todo
from project.models.todo    import TodoModel

class TodoInput(graphene.InputObjectType):
    todo = graphene.String()

class CreateTodoMutation(graphene.Mutation):
    todo = graphene.Field(Todo)

    class Arguments:
        todoInput = TodoInput(required=True)

    def mutate(self, info, todoInput=None):
        result = TodoModel(**todoInput).save()
        return CreateTodoMutation(todo=result)