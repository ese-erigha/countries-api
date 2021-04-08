from flask import Flask
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

# Globally accessible libraries
db = MongoEngine()

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config["MONGO_URI"] = "mongodb://localhost:27017/countries_api_dev"
    # app.config.from_object('project.config.Config')
    app.config['MONGODB_SETTINGS'] = {
        'host':'mongodb://localhost/countries_api_dev'
    }

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from .routes.home import home_blueprint
        from .routes.todo import todo_blueprint
        from .routes.country import country_blueprint

        # Register Blueprints
        app.register_blueprint(home_blueprint, url_prefix='/home')
        app.register_blueprint(todo_blueprint, url_prefix='/todo')
        app.register_blueprint(country_blueprint, url_prefix='/country')

        return app
