from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth
from functools import lru_cache
from .base_client import PropertyDetailClient
from .exceptions import UnavailableDataException
from app.schemas import HouseCanaryPropertyAddressSchema
from .property_detail_provider import PropertyDetailProvider


class HouseCanaryClient(PropertyDetailClient):
    def __init__(self, timeout=9.1):
        super().__init__("https://api.housecanary.com/v2", timeout)
        self.auth = HTTPBasicAuth(
            dotenv_values(".env.secret")["HOUSECANARY_API_KEY"],
            dotenv_values(".env.secret")["HOUSECANARY_API_SECRET"]
        )
        
    @property
    def provider(self):
        return PropertyDetailProvider.HOUSECANARY

    # Caching the results of the property/details endpoint because the payload
    # contains a wide assortment of useful information beyond sewer type,
    # and why not save this for later without another expensive call.
    # Using lru_cache as an example, but a cache with TTL expiry settings would
    # be used in reality, often an external KV db like redis.
    @lru_cache(1000)
    def get_property_details(self, **address_fields):
        """
            Requests the full property details from the external service.
            Assumes a valid set of required property search parameters.
        """
        ENDPOINT = "/property/details"
        address = HouseCanaryPropertyAddressSchema().dump(address_fields)
        response = self.session.get(f"{self.url}{ENDPOINT}", params=address, auth=self.auth, timeout=self.timeout)
        data = response.json()
        if data["property/details"]["api_code"] == 204:
            raise UnavailableDataException("HouseCanary missing property details for given address.")
        return data

    def get_sewer_type(self, **address_fields):
        """
            Extract sewer type information from cached property details 
            (read-through) from external service.
            Assumes a valid set of required property search parameters.
        """
        property_details = self.get_property_details(**address_fields)
        try:
            return {"sewer": property_details["property/details"]["result"]["property"]["sewer"]}
        except KeyError:
            raise UnavailableDataException("HouseCanary missing sewer data for given address.")
