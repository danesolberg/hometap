from app.schemas import BasePropertyAddressSchema
from app.clients import property_detail_client
from .mappers.property_details_mapper import PropertyDetailsMapper


class PropertyDetailsService:
    def get_sewer_type(self, address: BasePropertyAddressSchema):
        sewer_type = property_detail_client.get_sewer_type(**address)
        return PropertyDetailsMapper.to_domain(property_detail_client.provider, sewer_type)