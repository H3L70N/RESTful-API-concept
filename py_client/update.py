import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "New title",
    "price": 120.99,
}

response = requests.put(endpoint, json=data)

# print(response.headers)
# print(response.text)
print(response.json())
print(response.status_code)
