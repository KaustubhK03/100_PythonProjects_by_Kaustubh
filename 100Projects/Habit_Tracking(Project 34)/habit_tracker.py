import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

PIXELA_TOKEN = "Your pixela token goes here"
PIXELA_USERNAME = "your pixela username goes here"
PIXELA_GRAPH_ID = "your graph id goes here"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": PIXELA_GRAPH_ID,
    "name": "coding tracker",
    "unit": "minutes",
    "type": "int",
    "color": "momiji",
}

graph_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
# print(graph_response.text)

post_a_pixel_endpoint = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"

today = datetime.datetime.now()

# print(today.strftime("%Y%m%d"))

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? "),
}

pixel_response = requests.post(url=post_a_pixel_endpoint, json=pixel_params, headers=graph_headers)
print(pixel_response.text)

# Updating a Pixel by the PUT method

put_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today.strftime('%Y%m%d')}"

put_params = {
    "quantity": "300",
}

# put_response = requests.put(url=put_endpoint, json=put_params, headers=graph_headers)
# print(put_response.text)

# Delete a Pixel
del_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(url=del_endpoint, headers=graph_headers)
# print(response.text)
