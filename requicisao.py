import requests

r = requests.post('http://127.0.0.1:8000/items/?name=caio')

print(r.text)
