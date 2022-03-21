from marshmallow import Schema, fields, validates_schema, ValidationError

class BasePropertyAddressSchema(Schema):
    """
        A data marshalling class to validate that required properties exist
        to uniquely identify a US address.
    """
    address1_number = fields.String(required=True)
    address1_street = fields.String(required=True)
    address2 = fields.String(required=False)
    unit = fields.String(required=False)
    city = fields.String(required=False)
    state = fields.String(required=False)
    zip = fields.String(required=False)

    @validates_schema
    def identifies_unique_address(self, data, **kwargs):
        if 'zip' not in data and ('city' not in data or "state" not in data):
            raise ValidationError("US address requires either a zipcode or city/state combination.")