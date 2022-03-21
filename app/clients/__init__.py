from dotenv import dotenv_values
from app.clients.housecanary_client import HouseCanaryClient
from app.clients.property_detail_provider import PropertyDetailProvider

PRIMARY_API = dotenv_values(".env")["PRIMARY_PROPERTY_DETAIL_SOURCE"]

def create_property_detail_client():
    if PRIMARY_API == PropertyDetailProvider.HOUSECANARY.value:
        return HouseCanaryClient()
    else:
        raise NotImplementedError(
            f"Client not implemented for external service: {PRIMARY_API}")

property_detail_client = create_property_detail_client()