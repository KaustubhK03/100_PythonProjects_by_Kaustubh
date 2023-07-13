from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()

sheet_data = data_manager.print_data()

flight_search = FlightSearch()

noti_manager = NotificationManager()


for city in sheet_data:
    code = flight_search.iatacode_generator(city)
    city["iataCode"] = code
    data_manager.iataCode_updater(city)
city_dict = {}
for city in sheet_data:
    flight_data = flight_search.flight_searching(city)
    all_flights_data = FlightData(flight_data)
    city_wise_data = all_flights_data.structure_flight_data(flight_data)
    if city_wise_data is not None:
        city_dict = {key: int(value["Price"]) for (key, value) in city_wise_data.items()}
        lst = []
        for items in city_dict.items():
            lst.append(items)
        noti_manager.Check_if_there_are_cheap_flights(
            tuple_item=lst,
            city=city,
            flight_data=all_flights_data,
            data=flight_data
        )

