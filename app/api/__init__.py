from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

from app.api.resources.sewer import SewerType

api.add_resource(SewerType, "/propertydetails/sewer")