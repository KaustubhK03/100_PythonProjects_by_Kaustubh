import requests
from datetime import datetime

NUTRITIONX_APP_ID = "your appid goes here"
NUTRITIONX_API_KEY = "your api key goes here"

GENDER = "Your gender"
WEIGHT = "Your weight"
HEIGHT = "Your height"
AGE = "Your age"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
BEARER_TOKEN = "Your Sheety bearer token goes here"

query = input("Tell me what exercise did you do today?")

nutritionx_headers = {
    "x-app-id": NUTRITIONX_APP_ID,
    "x-app-key": NUTRITIONX_API_KEY,
}

post_requests = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=post_requests, headers=nutritionx_headers)
response.raise_for_status()
data = response.json()

todays_date = datetime.now().strftime("%d/%m/%Y")
time_rn = datetime.now().strftime("%X")


sheety_post_endpoint = "https://api.sheety.co/7218e9f661e2814d56dcc2b79e44303b/kaustubhWorkouts/workouts"

for exercise in data["exercises"]:
    sheety_requests = {
        "workout": {
            "date": todays_date,
            "time": time_rn,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    sheety_response = requests.post(url=sheety_post_endpoint, json=sheety_requests, headers=sheety_headers)
    sheety_response.raise_for_status()
