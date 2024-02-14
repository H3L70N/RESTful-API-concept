import requests

product_id = input("Product Id: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not valid id")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"
    response = requests.delete(endpoint)

    # print(response.headers)
    # print(response.json())
    print(response.status_code, response.status_code == 204)
