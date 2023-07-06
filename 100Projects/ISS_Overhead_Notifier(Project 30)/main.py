import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 22.719568
MY_LONG = 75.857727
email = "kalambkarkaustubh@gmail.com"
password = "saanixjuyiwicsrp"


def is_iss_above():
    req_for_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    req_for_iss.raise_for_status()
    data = req_for_iss.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


def is_night_time():
    time.sleep(60)
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0,
    }
    request = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    request.raise_for_status()
    data = request.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    if is_night_time() and is_iss_above():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email, msg="Subject:Look Up👆\n\nThe ISS is above you")
