import requests



while True:
    response = requests.get('http://localhost:8000/api/products/1')
    print(response.text)