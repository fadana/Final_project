import requests
import random
def generate_token():
    nr = random.randit(1, 99999999999999)
    request_body = {
        {
   "clientName": "Fader",
   "clientEmail": "fader@example(nr).com"
}}
        response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=request_body)
    token = response.json()["accessToken"]
