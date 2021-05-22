import os

from flask import Flask
from flask_cors import CORS
from mongoengine import connect
from flask_graphql import GraphQLView
from elasticsearch_dsl.connections import connections

from .graphql.middleware import build_middleware
from .graphql.schema import schema
from .config import ProductionConfig, DevelopmentConfig, LocalConfig


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.debug = True

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, middleware=build_middleware())
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
        connection_string = "mongodb://{username}:{password}@{host}:{port}/{db_name}?authSource=admin". \
            format(username=app.config["DB_USERNAME"], password=app.config["DB_PASSWORD"], host=app.config["DB_HOST"],
                   port=app.config["DB_PORT"], db_name=app.config["DB_NAME"])
        db = connect(host=connection_string)

    """Connect to ElasticSearch"""
    elastic_host = app.config["ELASTICSEARCH_HOST"]

    if mode == "local":
        connections.create_connection(hosts=[elastic_host])
    else:
        elastic_auth = "{username}:{password}".format(username=app.config["ELASTIC_USERNAME"],
                                                      password=app.config["ELASTIC_PASSWORD"])
        connections.create_connection(hosts=[elastic_host], http_auth=elastic_auth)

    with app.app_context():
        # Include our Routes
        from .routes.country import country_blueprint

        cors = CORS()
        cors.init_app(app, origins=["*"])

        # Register Blueprints
        app.register_blueprint(country_blueprint, url_prefix='/country')

        return app
