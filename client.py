import requests


response = requests.get('http://127.0.0.1:8080/adv/1')
print(response.status_code)
print(response.text)
