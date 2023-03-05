import requests
from Requests_folder.get.token import generate.token
def submit.order(bookid,customer_name):
request.body = {
"bookId": bookid,
   "CustomerName": customer_name
}
token = generate.token ()
header_params = {'Authorization':token}
response = requests.post("https://simple-books-api.glitch.me/orders", json=request_body, headers=hearder_params)
token = response.json()"accessToken"
return token