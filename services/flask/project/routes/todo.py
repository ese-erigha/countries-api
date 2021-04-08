from flask import Blueprint, jsonify, request
from flask import current_app as app
from project.services.todo import insertTodo, fetchTodos 

# Blueprint Configuration
todo_blueprint = Blueprint(
    'todo_blueprint', __name__,
)

@todo_blueprint.route('/list', methods=['GET'])
def getTodos():
    data = fetchTodos()
    return jsonify(status=True, data=data),200

@todo_blueprint.route('/create', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    todo = insertTodo(data)
    return jsonify(
        status=True,
        todo=todo,
        message='To-do saved successfully!'
    ),201