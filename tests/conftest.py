from pytest import fixture
from unittest.mock import patch
from app.clients.housecanary_client import HouseCanaryClient
from app.schemas import HouseCanaryPropertyAddressSchema, BasePropertyAddressSchema
from app.service import PropertyDetailsService


@fixture
def base_address():
    address = BasePropertyAddressSchema().dump({
        "address1_number": "123",
        "address1_street": "Main St",
        "zip": "94132"
    })
    return address

@fixture
def housecanary_address():
    address = HouseCanaryPropertyAddressSchema().dump({
        "address1_number": "123",
        "address1_street": "Main St",
        "zip": "94132"
    })
    return address

@fixture
def patch_session_object():
    patcher = patch("app.clients.base_client.Session.get")
    yield patcher

@fixture
def housecanary_client():
    return HouseCanaryClient()

@fixture
def property_details_service():
    return PropertyDetailsService()