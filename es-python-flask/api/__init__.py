from flask import Flask
from flask_restful import Api
from api.resources.hotels.hotel_search_api import HotelSearchAPI
from dotenv import load_dotenv
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

load_dotenv()

app = Flask(__name__)
app.secret_key = 'udemyESPython'
api = Api(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Udemy Python ElasticSearch',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
})

api.add_resource(HotelSearchAPI, '/hotels/search')

docs = FlaskApiSpec(app)
docs.register(HotelSearchAPI)

if __name__ == '__main__':
    app.run(debug=True)

from api import routes # noqa
