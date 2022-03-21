from requests import Response
import json
from tests.testdata import HOUSECANARY_PROPERTY_DETAILS


def test_get_sewer_type(
    base_address,
    patch_session_object,
    property_details_service
):
    with patch_session_object as mocked_get:
        resp = Response()
        resp._content = json.dumps(HOUSECANARY_PROPERTY_DETAILS).encode("utf-8")
        mocked_get.return_value = resp
        response = property_details_service.get_sewer_type(base_address)
        mocked_get.assert_called_once()
        assert response == {"sewer_type": "sewer"}