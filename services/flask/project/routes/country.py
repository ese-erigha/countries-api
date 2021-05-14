import json
import requests
from flask import Blueprint, jsonify, request, current_app as app
# from flask_cors import CORS

from project.models.country import CountryModel
from project.services.country import save_country
from project.elasticSearch.country import index_country, init_index as country_indexer_init

# Blueprint Configuration
country_blueprint = Blueprint(
    'country_blueprint', __name__,
)
# CORS(country_blueprint)


def create_country(country_data):
    country = save_country(country_data)
    country_dict = json.loads(country)
    index_country(country_dict)


def fetch_country_list_from_api():
    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.get(url, headers={'Content-Type': 'application/json; charset=utf-8'})
    country_list = response.json()
    return country_list


def store_data(country_list):
    country_indexer_init()
    for num, country in enumerate(country_list):

        print(num + 1)
        try:
            create_country(country)
        except BaseException as err:
            print(str(err))
            print(country['name'])
        print()


@country_blueprint.route('/data/load', methods=['POST'])
def build_country_data():
    auth_token = request.headers.get('Authorization')
    if auth_token != app.config["AUTH_TOKEN"]:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

    num_of_country = CountryModel.objects.count()
    if num_of_country == 250:
        return jsonify({"message": "Data already exists"}), 200

    country_list = fetch_country_list_from_api()
    store_data(country_list)
    return jsonify(country_list), 200
