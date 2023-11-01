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
api_key = 'AIzaSyDwh-rt_rOBI3qhUZwaFiHN0Qba4zyVZwc'
class GeocodingAPI:
    class _Read(Resource):
        def get(zipcode):
            try:
                return 'No results found for ' + zipcode
            except:
                return 0
        def post(data):
            map_client = googlemaps.Client(api_key)
            search_string = 'art museums near'
            response = map_client.textsearch(
                query=search_string,
                fields = ["formatted_address","name","rating","opening_now"],
                )
            results = response.get('results')
            return results
api.add_resource(GeocodingAPI._Read, '/<string:zip_code>')



