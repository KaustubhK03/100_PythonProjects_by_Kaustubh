import requests

SHEETY_URL = "https://api.sheety.co/8e28f8edbed9ec664c259e0129e010eb/cheapFlightDealsByKaustubh/prices"


class DataManager:
    def __init__(self):
        self.flight_data = {}

    def print_data(self):
        get_response = requests.get(url=SHEETY_URL)
        get_response.raise_for_status()
        data = get_response.json()["prices"]
        self.flight_data = data
        return self.flight_data

    def iataCode_updater(self, city):
        put_json = {
            "price": {
                "iataCode": city["iataCode"]
            }
        }
        put_response = requests.put(url=f"{SHEETY_URL}/{city['id']}", json=put_json)
