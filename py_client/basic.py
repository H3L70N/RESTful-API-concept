import requests

endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, json={"title": "Hello world"})

# print(response.headers)
# print(response.text)
print(response.json())
print(response.status_code)
