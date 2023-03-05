import requests

put_data = {'title': "Updated Book", "author": "Updated Author"} #put - actualizarea resursei in intregime
response = requests.put("http://books-api.example.com/books/1", json=put_data)
assert response.status_code ==200
assert response.json()[title] == 'Updated Book'
