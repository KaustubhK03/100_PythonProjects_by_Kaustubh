KIWI_API_KEY = "bLIxyn_R33CPcBiPF6brPgDcOiwqV7tw"


header = {
    "apikey": KIWI_API_KEY
}


class FlightData:
    def __init__(self, flight_data):
        try:
            self.price = flight_data["data"][0]["price"]
            self.departure_airport_code = flight_data["data"][0]["flyFrom"]
            self.departure_city = flight_data["data"][0]["cityFrom"]
            self.destination_city = flight_data["data"][0]["cityTo"]
            self.destination_airport_code = flight_data["data"][0]["flyTo"]
            self.outbound_date = flight_data["data"][0]["route"][0]["local_departure"].split("T")[0]
            self.inbound_date = flight_data["data"][0]["route"][1]["local_departure"].split("T")[0]
            self.stop_overs = 2
            self.via_city = flight_data['data'][0]['route'][0]['cityTo']
            self.via_city_airport_code = flight_data['data'][0]['route'][0]['cityCodeTo']
            self.available_cities = {}
        except IndexError and TypeError:
            pass

    def structure_flight_data(self, flight_data):
        try:
            if flight_data['data'][0]['availability']['seats'] is not None:
                self.available_cities[f"{flight_data['data'][0]['cityTo']}"] = {"Price": f"{flight_data['data'][0]['price']}"}
                return self.available_cities
        except TypeError:
            pass
