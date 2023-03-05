import requests

def get_all_books(type="",limit=20):
		response = ""
		if type=="" and limit == 20:
				response = requests.get("https://simple-books-api.glitch.me/books")
		elif type != "" and limit ==20:
				response = requests.get(f"https://simple-books-api.glitch.me/books?type={type}")
		elif type == "" and limit !=20:
				response = requests.get(f"https://simple-books-api.glitch.me/books?limit={limit}")
		else:
				response = requests.get(f"https://simple-books-api.glitch.me/books?limit={limit}&type={type}")
		return response