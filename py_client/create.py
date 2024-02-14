import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "New Stuff",
    "content": "Testing api alt view",
    "price": 32.99,
}

response = requests.post(endpoint, json=data)


# print(response.headers)
# print(response.text)
print(response.json())
print(response.status_code)