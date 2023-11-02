from flask import Flask, jsonify, request
import requests
import pgeocode
import googlemaps

app = Flask(__name__)
places_api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
api_key = 'AIzaSyDwh-rt_rOBI3qhUZwaFiHN0Qba4zyVZwc'
    
def initGeocoding(postalcode,country):
      
    nomi = pgeocode.Nominatim(country)
    postal_code = postalcode
    location = nomi.query_postal_code(postalcode)
    print("coordinates")
    print(location.latitude, location.longitude)
    latitude = location.latitude
    longitude = location.longitude
      
    print(latitude)

    #places_api_url ="https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=restaurent&location=-33.8670522,151.1957362&radius=1500&type=restaurant&key="+api_key
    places_api_url ="https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=art museum&location="+str(latitude)+","+str(longitude)+"&radius=1500&type=art museum&key="+api_key
    
    params = {
        'keyword': 'restaurent',
        'location': {'latitude' : latitude ,'longitude' : longitude},
        'radius': 1000000,
        'key': api_key,
    }
    
    response = requests.get(places_api_url, params=params)
    results = response.json().get('results',[])
    #print("results")
    #print(response.json())   

    print(results)
        
    museums_info = []
    for result in results:
        museum_info = {
            'name': result.get('name'),
            'vicinity': result.get('vicinity'),
            #'rating': result.get('rating', 'N/A'),
            #'open': result.get('opening_now'),
        }
        museums_info.append(museum_info)
    return museums_info 
    

def searchMuseums(zipcode):
    museums_info = initGeocoding(zipcode,'US')
    return jsonify({'art_museums': museums_info})
if __name__ == '__main__':
    app.run()





