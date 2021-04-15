from flask import Flask
# from flask_mongoengine import MongoEngine
from mongoengine import connect
from flask_graphql import GraphQLView
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Index
from .elasticSearch    import todo as todoES
from .graphql.schema import schema

def create_app():
    """Instantiate database"""
    db = connect(db="countries_api_dev", host="localhost")

    """Drop all collections"""
    # https://stackoverflow.com/questions/15886469/dropping-all-collections-in-mongoengine
    try:
        db.drop_database("countries_api_dev")
    except BaseException as err:
        print(err)

    """Connect to ElasticSearch"""
    connections.create_connection(hosts=['localhost'])

    todoES.init()

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
