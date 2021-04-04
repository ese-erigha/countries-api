from flask import Blueprint, jsonify
from flask import current_app as app
from project.models import User

# Blueprint Configuration
home_blueprint = Blueprint(
    'home_blueprint', __name__,
)

@home_blueprint.route('/', methods=['GET'])
def home():
    """Homepage."""
    return jsonify(hello="world")