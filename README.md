# Hometap Property API
Example approach for service that wraps an external API.

## Dependencies
- Flask - lightweight web application framework
- Marshmallow - data marshalling and (de)serialization
- Pytest - testing framework

## How to run
- create a virtualenv `python3 -m venv hometap`
- install dependencies `pip install -r requirements.txt`
- create a `.env.secret` file to store credentials (see Configuration)
- run the flask app `source run.sh`
- access the service at `127.0.0.1:5000`

## Configuration
A `.env.secret` file must be created to hold API credentials.  Create this file with the following format:
```
HOUSECANARY_API_KEY = "enter_real_key"
HOUSECANARY_API_SECRET = "enter_real_secret"
```

## Run tests
- Run unit tests with `pytest -k unit`
- Run integration tests with `pytest -k integration` (note: these will fail until proper API credentials are setup)

## Endpoints

Endpoint: `/propertydetails/sewer`

Method: `GET`

Arguments:
- `address1_number` - road number of the requested address (required)
- `address1_street` - road name of the requested address (required)
- `address2` - additional address components (optional)
- `unit` - building unit number of requested address (optional)
- `city` - city name of the requested address (optional)
- `state` - US state name of the requested address (optional)
- `zip` - ZIP code of the requested address (optional)

*parameters must include either a zip code or a city/state combination*

## Structure
- `/api` - routes for wrapper API
- `/clients` - client code to accessing external APIs (HouseCanary, etc.)
- `/schemas` - domain object schemas for data validation / marshalling
- `/service` - service layer to connect client and api layers and run business logic
