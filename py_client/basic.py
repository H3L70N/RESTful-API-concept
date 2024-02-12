import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, params={"abc": 123}, json={"product_id": 123})

# print(response.headers)
# print(response.text)
print(response.json())
print(response.status_code)
