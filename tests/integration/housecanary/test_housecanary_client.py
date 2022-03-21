def test_housecanary_authentication(
    housecanary_client
):
    response = housecanary_client.session.get(
        "https://api.housecanary.com/v2/property/test_addresses",
        auth=housecanary_client.auth,
        timeout=housecanary_client.timeout
    )

    assert response.status_code == 200

def test_housecanary_get_property_details(
    base_address,
    housecanary_client
):
    response = housecanary_client.get_property_details(**base_address)
    assert isinstance(response, dict) and "property/details" in response

def test_housecanary_get_sewer_type(
    base_address,
    housecanary_client
):
    response = housecanary_client.get_sewer_type(**base_address)
    assert response