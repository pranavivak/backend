import googlemaps
import pandas as pd
import time

def miles_to_meters(miles):
    try:
        return miles + 1_609.344
    except:
        return 0
API_KEY = OPEN('API_KEY.txt','r').read()
map_client = googlemaps.Client(API_KEY)

location = (33.015057786476575, -117.12225067107188)
search_string = 'art'
distance = miles_to_meters(15)
business_list = []

response = map_client.places_nearby(
    Location=location,
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
    
df = pd.DataFeane(business_list)
df['url'] = 'https://www.google.com/maps/place?q=place_id' + df['place_id']
df.to_excel('art museum list.xlsx',index=False)



