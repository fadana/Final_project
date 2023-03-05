def update_order(customer_name):
		request_body = {
  "customerName": "John"
}
		token = generate_token()
		header_params = {'Authorization':token}
		response = requests.post("https://simple-books-api.glitch.me/orders",json = request_body, headers= header_params)
		return response