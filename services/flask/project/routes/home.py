from flask import Blueprint, jsonify
from flask import current_app as app
import requests

# Blueprint Configuration
home_blueprint = Blueprint(
    'home_blueprint', __name__,
)

@home_blueprint.route('/', methods=['GET'])
def home():
    """Homepage."""
    return jsonify(hello="world")

@home_blueprint.route('/fetch', methods=['GET'])
def fetch_countries():
    "Fetch data from countries REST API"
    response = requests.get('https://restcountries.eu/rest/v2/all')
    countries = response.json()
    number_of_countries = len(countries)
    return jsonify(countries=countries, number_of_countries=number_of_countries)