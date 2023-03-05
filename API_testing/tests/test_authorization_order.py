import requests

class test_authorisation_order:
    def test_authorisation_order(self):
        response = requests.post("https://simple-books-api.glitch.me/orders", json=request_body, headers=header_params)
        auth_header = {"Authorization": "289fcc9f7b9964d52c3651eb6dbfdefd748f2923db8cbb12182e425ad8f368db"}
          body = {
    "bookId": 1,
    "customerName": "John"
}

       response = requests.post(url, headers=auth_header, json=body)

       assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
       assert "bookId" in response.json(), "Response body does not contain bookId field"
