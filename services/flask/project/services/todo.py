from project.models.todo import Todo

def fetchTodos():
    # todos = Todo.objects().to_json()
    todos = Todo.objects()
    return todos

def insertTodo(data):
    todo = Todo(**data).save()
    return todo

