from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes import request_api


swagger_url = '/swagger'
api_url = '/static/swagger.json'
swagger_ui = get_swaggerui_blueprint(swagger_url,
                                     api_url,
                                     config={
                                         'app_name': "Infostud API"
                                     })


def create_app(debug=False):
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(swagger_ui)
    app.register_blueprint(request_api.get_blueprint())
    app.debug = debug
    return app


app = create_app(debug=True)

app.run(host='0.0.0.0')
