from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import requests

# Function to fetch department details from the Metropolitan Museum of Art API
def get_departments():
    api_url = 'https://collectionapi.metmuseum.org/public/collection/v1/departments'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('departments', [])
    else:
        return []

# Blueprint and API instance for department details
departments_api = Blueprint('departments_api', __name__, url_prefix='/api/departments')
api = Api(departments_api)

# Resource class for reading department details
class DepartmentsAPI(Resource):
    def get(self):
        return jsonify(get_departments())

# Adding the resource to the API
api.add_resource(DepartmentsAPI, '/')

if __name__ == "__main__":
    # Change this to your server URL
    server = 'https://flask.nighthawkcodingsociety.com'
    url = server + "/api/departments"
    responses = []

    # Get department details from the Metropolitan Museum of Art API
    responses.append(requests.get(url))

    for response in responses:
        print(response)
        try:
            print(response.json())
        except Exception as e:
            print(f"Error: {e}")
