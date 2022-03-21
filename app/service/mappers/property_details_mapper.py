from app.clients import PropertyDetailProvider

class PropertyDetailsMapper:
    mappings = {
        PropertyDetailProvider.HOUSECANARY: {
            "heating_type": {
                "from_field": "heating",
                # HouseCanary documentation of property detail field values
                # is wrong based on example endpoint output.  Just sticking
                # with the claimed values, but these probably need to be tested
                # against production api results.
                "conversions": {
                    "baseboard": "boiler",
                    "central": "furnace", 
                    "coal": "other", 
                    "convection": "other", 
                    "electric": "electric",
                    "Floor/Wall": "other" 
                    "forced_air_unit", 
                    "gas": "gas", 
                    "geo-thermal": "heat pump", 
                    "gravity": "other", 
                    "heat_pump": "heat pump", 
                    "hot_water": "boiler", 
                    "none": "none", 
                    "oil": "oil", 
                    "other": "unknown", 
                    "partial": "none", 
                    "propane": "other", 
                    "radiant": "boiler", 
                    "solar": "other", 
                    "Space/Suspended": "unknown", 
                    "steam": "other", 
                    "vent": "unknown", 
                    "wood_burning": "wood burning", 
                    "yes": "unknown", 
                    "zone": "unkown"
                }
            },
            "pool": {
                "from_field": "pool",
                "conversions": None,
            },
            "room_count": {
                "from_field": "total_number_of_rooms",
                "conversions": None
            },
            "sewer_type": {
                "from_field": "sewer",
                "conversions": {
                    "municipal": "sewer",
                    "none": "none",
                    "storm": "unknown",
                    "septic": "septic",
                    "yes": "unknown"
                }
            }
        }
    }

    @classmethod
    def to_domain(cls, provider: PropertyDetailProvider, external_data):
        domain_data = {}
        for domain_field, map_config in cls.mappings[provider].items():
            external_field = map_config["from_field"]
            if external_field in external_data:
                field_data = external_data[external_field]
                convs = map_config["conversions"]
                if convs is None:
                    domain_data[domain_field] = field_data
                else:
                    domain_data[domain_field] = convs[field_data]
        return domain_data