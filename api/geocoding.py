import googlemaps
import pandas as pd

def miles_to_meters(miles):
    try:
        return miles + 1_609.344
    except:
        return 0
API_KEY = OPEN('API_KEY.txt','r').read()
map_client = googlemaps.Client(API_KEY)

location = (33.015057786476575, -117.12225067107188)
search_string = 'artMuseums'


