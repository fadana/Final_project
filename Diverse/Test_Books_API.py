import requests

# Test the GET /books endpoint
response = requests.get("https://api.example.com/books")
assert response.status_code == 200
assert len(response.json()) > 0

# Test the GET /books/{id} endpoint
response = requests.get("https://books-api.example.com/books/1")
assert response.status_code == 200
assert response.json()["id"] == 1

# Test the POST /books endpoint
data = {"title": "Test Book", "author": "Test Author"}
response = requests.post("https://books-api.example.com/books", json=data)
assert response.status_code == 201
assert response.json()["title"] == "Test Book"

# Test the PUT /books/{id} endpoint
data = {"title": "Updated Book", "author": "Updated Author"}
response = requests.put("https://books-api.example.com/books/1", json=data)
assert response.status_code == 200
assert response.json()["title"] == "Updated Book"

# Test the DELETE /books/{id} endpoint
response = requests.delete("https://books-api.example.com/books/1")
assert response.status_code == 204




