import os

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from .elasticSearch import connection as es_connection

from .graphql.middleware import build_middleware
from .graphql.schema import schema
from .config import ProductionConfig, DevelopmentConfig, LocalConfig
from .database import auto_connect as db_connect


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.debug = True

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, middleware=build_middleware())
    )

    """RETRIEVE APP CONFIG"""
    mode = os.getenv("MODE")

    if mode == "local":
        app.config.from_object(LocalConfig())
    elif mode == "development":
        app.config.from_object(DevelopmentConfig())
    else:
        app.config.from_object(ProductionConfig())

    """Instantiate database"""
    db_connect(app.config, mode)

    """Connect to ElasticSearch"""
    es_connection.connect(app.config, mode)

    with app.app_context():
        # Include our Routes
        from .routes.country import country_blueprint

        cors = CORS()
        cors.init_app(app, origins=["*"])

        # Register Blueprints
        app.register_blueprint(country_blueprint, url_prefix='/country')

        return app
