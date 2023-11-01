import json
import googlemaps
def initGeocoding(self,zipcode):
   self.zip = zipcode
def getPlaces(self,zip):
   zip = 92127
   api_key = 'AIzaSyDwh-rt_rOBI3qhUZwaFiHN0Qba4zyVZwc'
   map_client = googlemaps.Client(api_key)
   search_string = 'art museums near'+ 'zip'
   response = map_client.textsearch(
      query=search_string,
      fields = ["formatted_address","name","rating","opening_now"],
      )
   results = response.get('results')
   return (results)






