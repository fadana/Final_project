import requests

class test_authentication_order:
    def test_authentication_order(self):
        response = requests.post("https://simple-books-api.glitch.me/api-clients", json=request_body, headers=header_params)
        auth_header = {"Authorization": "289fcc9f7b9964d52c3651eb6dbfdefd748f2923db8cbb12182e425ad8f368db"}
          body = {
   "clientName": "Postman",
   "clientEmail": "valentin@example.com"
}