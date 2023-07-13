import requests
import datetime

KIWI_API_KEY = "your kiwi api kay"
kiwi_endpoint = "kiwi's location endpoint"
KIWI_SEARCH_ENDPOINT = "kiwi's search endpoint"

date_from = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
date_to = (datetime.datetime.now() + datetime.timedelta(6 * 30)).strftime("%d/%m/%Y")

kiwi_headers = {
            "apikey": KIWI_API_KEY,
        }
count = 0


class FlightSearch:
    def iatacode_generator(self, city):
        kiwi_params = {
            "term": city['city']
        }
        kiwi_get_response = requests.get(url=f"{kiwi_endpoint}", params=kiwi_params, headers=kiwi_headers)
        kiwi_get_response.raise_for_status()
        data = kiwi_get_response.json()
        code = data["locations"][0]['code']
        return code

    def flight_searching(self, city):
        search_params = {
            "fly_from": "IDR",
            "fly_to": city['iataCode'],
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR",
            "limit": 5,
        }
        kiwi_search_response = requests.get(url=KIWI_SEARCH_ENDPOINT, params=search_params, headers=kiwi_headers)
        data = kiwi_search_response.json()
        if data['_results'] == 0:
            return self.searching_flights_with_stopovers(city)
        else:
            return data

    def searching_flights_with_stopovers(self, city):
        new_search_params = {
            "fly_from": "IDR",
            "fly_to": city['iataCode'],
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 4,
            "curr": "INR",
            "limit": 5,
        }
        new_kiwi_search_response = requests.get(url=KIWI_SEARCH_ENDPOINT, params=new_search_params,
                                                headers=kiwi_headers)
        new_data = new_kiwi_search_response.json()
        return new_data
