import requests

url = "http://161.97.114.244:8090/v2/network/information"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")


import requests

url = "http://161.97.114.244:8090/v2/wallets/101b3814d6977de4b58c9dedc67b87c63a4f36dd/addresses"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

print("\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

import requests

url = "http://161.97.114.244:8090/v2/wallets"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)