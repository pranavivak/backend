from flask import Blueprint, jsonify 
from flask_restful import Api, Resource 
import googlemaps
import pandas as pd
import time

from model.geocoding import *

geocoding_api = Blueprint('geocoding_api', __name__,
                   url_prefix='/api/geocoding')

api = Api(geocoding_api)

class GeocodingApi:
    class _Create(Resource):
        def post(self, Artmuseums):
            pass
        
    class _Read(Resource):
        def get(self):
            return jsonify(getArtmuseums())

location = (33.014599007062486, -117.12140179432065)
search_string = 'art'
business_list = []

response = map_client.places_nearby(
    location=location,
    keyword=search_string,
    name='art museum',
    radius=distance,
)

business_list.extend(response.get('results'))
next_page_token = response.get('next_page_token')

while next_page_token:
    time.sleep(2)
    response = map_client.places_nearby(
        Location=location,
        keyword=search_string,
        name='art museum',
        radius=distance,
        page_taken=next_page_token
    )
    business_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')



