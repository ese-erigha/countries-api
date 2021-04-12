from flask import Flask
# from flask_mongoengine import MongoEngine
from mongoengine import connect
from flask_graphql import GraphQLView
from .graphql.schema import schema

def create_app():
    """Instantiate database"""
    connect(db="countries_api_dev", host="localhost")

    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.debug = True

    app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )

    with app.app_context():
        # Include our Routes
        from .routes.country import country_blueprint
        from .routes.todo import todo_blueprint

        # Register Blueprints
        app.register_blueprint(country_blueprint, url_prefix='/country')
        app.register_blueprint(todo_blueprint, url_prefix='/todo')

        return app
