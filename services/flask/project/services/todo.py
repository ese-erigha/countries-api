from project import mongo

def fetchTodos():
    _todos = mongo.db.todo.find()
    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'todo': todo['todo']
        }
        data.append(item)
    return data

def insertTodo(data):
    item = {
        'todo': data['todo']
    }
    mongo.db.todo.insert_one(item)
