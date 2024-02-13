import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done",
    "price": 32.99,
}

response = requests.post(endpoint, json=data)


# print(response.headers)
# print(response.text)
print(response.json())
print(response.status_code)