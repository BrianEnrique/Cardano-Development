import requests
import json

add1 = 'network'
add2 = 'information'
url = f"http://localhost:8090/v2/{add1}/{add2}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)