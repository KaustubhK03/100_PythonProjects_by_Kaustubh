from twilio.rest import Client
import smtplib
import requests

from_email = "kalambkarkaustubh@gmail.com"
APP_PASS = "saanixjuyiwicsrp"

SHEETY_GET_URL = "https://api.sheety.co/8e28f8edbed9ec664c259e0129e010eb/cheapFlightDealsByKaustubh/users"

account_sid = "ACf82a66f7c0ded5ac03bd424105e99d90"

auth_token = "5c327246ea276b97aab9b96c5a68203e"

client = Client(account_sid, auth_token)


class NotificationManager:
    def Check_if_there_are_cheap_flights(self, tuple_item, city, flight_data, data):
        for tup in tuple_item:
            # if city['city'] == tup[0]:
            if city['lowestPrice'] >= tup[1] and len(data['data'][0]['route']) / 2 == 1:
                self.send_mails(flight_data, tup)
                message = client.messages.create(
                    to="+917566564666",
                    from_="+16186346564",
                    body=f"Low Price Alert! Only {flight_data.price} rupees to fly from "
                         f"{flight_data.departure_city} {flight_data.departure_airport_code} to {tup[0]}-"
                         f"{flight_data.destination_airport_code} from {flight_data.outbound_date} to "
                         f"{flight_data.inbound_date}")
            elif city['lowestPrice'] >= tup[1] and len(data['data'][0]['route']) / 2 > 1:
                self.send_via_city_mails(flight_data, tup)
                message = client.messages.create(
                    to="+917566564666",
                    from_="+16186346564",
                    body=f"Low Price Alert! Only {flight_data.price} rupees to fly from {flight_data.departure_city}-"
                         f"{flight_data.departure_airport_code} to {tup[0]}-{flight_data.destination_airport_code} "
                         f"from {flight_data.outbound_date} to {flight_data.inbound_date}\n"
                         f"Flight has {flight_data.stop_overs} stopovers, via {flight_data.via_city}: "
                         f"{flight_data.via_city_airport_code}")

    def send_mails(self, flight_data, tup):
        get_request_response = requests.get(url=SHEETY_GET_URL)
        users_data = get_request_response.json()['users']
        for user in users_data:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=from_email, password=APP_PASS)
                connection.sendmail(
                    from_addr=from_email,
                    to_addrs=user['email'],
                    msg=f"Subject:Low Price Alert!\n\nOnly {flight_data.price} rupees to fly from "
                         f"{flight_data.departure_city} {flight_data.departure_airport_code} to {tup[0]}-"
                         f"{flight_data.destination_airport_code} from {flight_data.outbound_date} to "
                         f"{flight_data.inbound_date}"
                )

    def send_via_city_mails(self, flight_data, tup):
        get_request_response = requests.get(url=SHEETY_GET_URL)
        users_data = get_request_response.json()['users']
        for user in users_data:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=from_email, password=APP_PASS)
                connection.sendmail(
                    from_addr=from_email,
                    to_addrs=user['email'],
                    msg=f"Subject:Low Price Alert!\n\nLow Price Alert! Only {flight_data.price} rupees to fly from "
                        f"{flight_data.departure_city}-"
                        f"{flight_data.departure_airport_code} to {tup[0]}-{flight_data.destination_airport_code} "
                        f"from {flight_data.outbound_date} to {flight_data.inbound_date}\n"
                        f"Flight has {flight_data.stop_overs} stopovers, via {flight_data.via_city}: "
                        f"{flight_data.via_city_airport_code}"
                )


