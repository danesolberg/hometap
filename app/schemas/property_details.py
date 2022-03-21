from marshmallow import Schema, fields, validate

class PropertyDetails(Schema):
    """
        A domain representation of property details.
    """
    heating_type = fields.String(validate=validate.OneOf([
        "furnace", "boiler", "heat_pump", "electric", "gas", "oil", "other",
        "word burning", "none", "unknown"
    ]))
    pool = fields.Bool()
    room_count = fields.Int(validate=validate.Range(0, None))
    sewer_type = fields.String(validate=validate.OneOf([
        "sewer", "septic", "none", "unknown"
    ]))