from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from routes import blp as PredictBlueprint

def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Dummy Api"
    app.config['SECRET_KEY'] = 'key'
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


    api = Api(app)
    api.register_blueprint(PredictBlueprint)

    return app





