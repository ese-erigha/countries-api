from flask import Blueprint, jsonify, request
from flask import current_app as app
from project.services.country import addCountry, fetchCountries 

# Blueprint Configuration
country_blueprint = Blueprint(
    'country_blueprint', __name__,
)

@country_blueprint.route('/list', methods=['GET'])
def getCountries():
    data = fetchCountries()
    return jsonify(status=True, data=data)

@country_blueprint.route('/create', methods=['POST'])
def createCountry():
    data = request.get_json(force=True)
    addCountry(data)
    return jsonify(
        status=True,
        message='Country saved successfully!'
    )
