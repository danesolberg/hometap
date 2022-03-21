from requests import Response
import json
from tests.testdata import HOUSECANARY_PROPERTY_DETAILS


def test_get_property_details(
    base_address,
    patch_session_object,
    housecanary_client
):
    with patch_session_object as mocked_get:
        resp = Response()
        resp._content = json.dumps(HOUSECANARY_PROPERTY_DETAILS).encode("utf-8")
        mocked_get.return_value = resp
        response = housecanary_client.get_property_details(**base_address)
        mocked_get.assert_called_once()
        assert response == HOUSECANARY_PROPERTY_DETAILS

def test_get_sewer_type(
    base_address,
    patch_session_object,
    housecanary_client
):
    with patch_session_object as mocked_get:
        resp = Response()
        resp._content = json.dumps(HOUSECANARY_PROPERTY_DETAILS).encode("utf-8")
        mocked_get.return_value = resp
        response = housecanary_client.get_sewer_type(**base_address)
        mocked_get.assert_called_once()
        assert response == {"sewer": "municipal"}