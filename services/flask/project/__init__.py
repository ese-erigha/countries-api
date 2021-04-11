from flask import Flask
# from flask_mongoengine import MongoEngine
from mongoengine import connect
from flask_graphql import GraphQLView
from .graphql.schema import schema

# Globally accessible libraries
# db = MongoEngine()

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
    # app.config['MONGODB_SETTINGS'] = {
    #     'host':'mongodb://localhost/countries_api_dev'
    # }

    # Initialize Plugins
    # db.init_app(app)

    return app

    # with app.app_context():
    #     # Include our Routes
    #     from .routes.home import home_blueprint
    #     from .routes.todo import todo_blueprint
    #     from .routes.country import country_blueprint

    #     # Register Blueprints
    #     app.register_blueprint(home_blueprint, url_prefix='/home')
    #     app.register_blueprint(todo_blueprint, url_prefix='/todo')
    #     app.register_blueprint(country_blueprint, url_prefix='/country')

    #     return app
