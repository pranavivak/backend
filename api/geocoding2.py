from flask import Blueprint, jsonify 
from flask_restful import Api, Resource 
import googlemaps
import time
import json

from model.geocoding import *

geocoding_api = Blueprint('geocoding_api', __name__,
                   url_prefix='/api/geocoding')

api = Api(geocoding_api)

class GeocodingApi:
    class GeocodingCR(Resource):
        def post (self):
            body = request.get_json()
