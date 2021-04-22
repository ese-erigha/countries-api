from flask import Blueprint, jsonify

# Blueprint Configuration
home_blueprint = Blueprint(
    'home_blueprint', __name__,
)


@home_blueprint.route('/', methods=['GET'])
def home():
    """Homepage."""
    return jsonify(hello="world")
