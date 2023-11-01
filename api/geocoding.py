from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import googlemaps
import requests
import random
import json
from model.geocoding import *
geocoding_api = Blueprint('geocoding_api', __name__,
                           url_prefix='/api/geocoding')
# API generator
api = Api(geocoding_api)
class GeocodingAPI:
    class _Read(Resource):
        def get(self):
            return jsonify(getPlaces(zip))
api.add_resource(GeocodingAPI._Read, '/')
