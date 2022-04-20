from flask import Blueprint
from flask_restful import Api
from .resources import ReturnCompiled # post e get

bp = Blueprint("restapi", __name__, url_prefix="/api")
api = Api(bp)
# api.add_resource(ReturnCompiled, '/')

def init_app(app):
    app.register_blueprint(bp)
