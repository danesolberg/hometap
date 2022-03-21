from flask_restful import Resource
from flask import request, abort
import json
from app.schemas import BasePropertyAddressSchema
from app.service import PropertyDetailsService

service = PropertyDetailsService()

class SewerType(Resource):
    def get(self):
        input_schema = BasePropertyAddressSchema()
        errors = input_schema.validate(request.args)
        if errors:
            abort(400, str(errors))
        address = input_schema.dump(request.args)
        result = service.get_sewer_type(address)
        return json.dumps(result)