from project.models.todo import TodoModel

def fetchTodos():
    # todos = Todo.objects().to_json()
    todos = TodoModel.objects()
    return todos

def insertTodo(data):
    todo = TodoModel(**data).save()
    return todo

