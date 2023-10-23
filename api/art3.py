from flask import Flask, jsonify, Blueprint
from flask_restful import Api, Resource
import requests

rijksmuseum_api = Blueprint('rijksmuseum_api', __name__, url_prefix='/api/rijksmuseum')
api = Api(rijksmuseum_api)

class ArtworkAPI(Resource):
    def get(self, object_id):
        api_key = "YOUR_RIJKSMUSEUM_API_KEY"
        base_url = "https://www.rijksmuseum.nl/api/en/collection/"
        url = f"{base_url}{object_id}?key={api_key}"
        
        response = requests.get(url)
        data = response.json()

        # Process the data as needed
        artwork_info = {
            "title": data.get("artObject", {}).get("title", "Not Available"),
            "artist": data.get("artObject", {}).get("principalOrFirstMaker", "Not Available"),
            # Add more fields as needed
        }

        return jsonify(artwork_info)

api.add_resource(ArtworkAPI, '/artwork/<string:object_id>')

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(rijksmuseum_api)
    app.run(debug=True)
