import requests
import smtplib
import os

MY_LAT = "Your latitude a"
MY_LONG = "your longitude"
API_KEY = "Your own api key from the weatherapi website"
ENDPOINT = "http://api.weatherapi.com/v1/forecast.json"
email = "your mail goes here"
password = "You App password goes here"


weather_parameters = {
    "key": API_KEY,
    "q": "Indore"
}

lat_lon_parameters = {
    "key": API_KEY,
    "q": (MY_LAT, MY_LONG),
}

response = requests.get(url=ENDPOINT, params=lat_lon_parameters)
response.raise_for_status()
data = response.json()


next_12_hr_weather_lst = [data["forecast"]["forecastday"][0]["hour"][i]["condition"]["code"] for i in range(0, 12)]


def bring_umbrella(count=0):
    for weather_code in next_12_hr_weather_lst:
        if 1063 <= weather_code < 1135 or 1150 <= weather_code <= 1282:
            count += 1
        else:
            continue
    if count == 0:
        return False
    else:
        return True


if bring_umbrella():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg="Subject:Rain Alert\n\nIt's going to rain today remember to bring an Umbrella"
        )
