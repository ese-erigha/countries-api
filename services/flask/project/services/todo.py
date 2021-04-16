from project.models.todo import TodoModel


def fetch_todos():
    todos = TodoModel.objects().to_json()
    return todos


def save_todo(data):
    todo = TodoModel(**data).save()
    return todo.to_json()
