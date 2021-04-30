import os

from flask import Flask
from mongoengine import connect
from flask_graphql import GraphQLView
from elasticsearch_dsl.connections import connections
from .graphql.schema import schema
from .config import ProductionConfig, DevelopmentConfig, LocalConfig


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.debug = True

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )

    mode = os.getenv("MODE")

    if mode == "local":
        app.config.from_object(LocalConfig())
    elif mode == "development":
        app.config.from_object(DevelopmentConfig())
    else:
        app.config.from_object(ProductionConfig())

    """Instantiate database"""
    if mode == "local":
        db = connect(db=app.config["DB_NAME"], host=app.config["DB_HOST"])  # localhost
    else:
        connection_string = app.config["DB_HOST"] + "://" + app.config["DB_USERNAME"] + \
                            ":" + app.config["DB_PASSWORD"] + "@127.0.0.1:" + app.config["DB_PORT"] + "/" + \
                            app.config["DB_NAME"] + "?authSource=" + app.config["DB_NAME"]
        db = connect(host=connection_string)  # docker
    # db = connect(db="countries_api_dev", host="mongodb", port=27017)

    """Drop all collections"""
    # https://stackoverflow.com/questions/15886469/dropping-all-collections-in-mongoengine
    try:
        db.drop_collection("country")
        db.drop_collection("todo")
        # db.drop_database("countries_api_dev")
        # db.drop_database(app.config["DB_NAME"])
    except BaseException as err:
        print(err)

    """Connect to ElasticSearch"""
    connections.create_connection(hosts=[app.config["ELASTICSEARCH_HOST"]])
    # connections.create_connection(hosts=['localhost'])  # localhost
    # connections.create_connection(hosts=['elasticsearch']) # docker

    with app.app_context():
        # Include our Routes
        from .routes.country import country_blueprint

        # Register Blueprints
        app.register_blueprint(country_blueprint, url_prefix='/country')

        return app
