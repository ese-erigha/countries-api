import json
from flask import Blueprint, request, Response
from project.services.country import save_country, fetch_countries
from project.elasticSearch.country import index_country

# Blueprint Configuration
country_blueprint = Blueprint(
    'country_blueprint', __name__,
)


@country_blueprint.route('/list', methods=['GET'])
def get_countries():
    countries = fetch_countries()
    return Response(countries, mimetype="application/json", status=200)


@country_blueprint.route('/create', methods=['POST'])
def create_country():
    data = request.get_json(force=True)
    country = save_country(data)
    country_dict = json.loads(country)
    index_country(country_dict)
    return Response(country, mimetype="application/json", status=201)
