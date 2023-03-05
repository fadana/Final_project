import requests

import requests

from API_testing.Requests_folder.get_token import generate_token


def update_order(customer_name):
		request_body = {
  "customerName": "John"
}
		token = generate_token()
		header_params = {'Authorization':token}
		response = requests.patch("https://simple-books-api.glitch.me/orders",json = request_body, headers= header_params)
		return response