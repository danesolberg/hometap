from marshmallow import fields
from .baseaddress import BasePropertyAddressSchema


class HouseCanaryPropertyAddressSchema(BasePropertyAddressSchema):
    """
        Conforms address data to the HouseCanary standard.
    """
    class Meta:
        fields = ["address", "unit", "city", "state", "zipcode"]
        load_only = ["address1_number", "address1_street"]

    address = fields.Method("build_address")
    unit = fields.String(required=False)
    city = fields.String(required=False)
    state = fields.String(required=False)
    zipcode = fields.String(required=False, attribute="zip")

    def build_address(self, obj):
        return obj["address1_number"] + " " + obj["address1_street"]