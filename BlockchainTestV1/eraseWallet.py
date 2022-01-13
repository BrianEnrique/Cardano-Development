import requests
import json

from requests.api import delete

#url = "http://161.97.114.244:8090/v2/wallets/1c5984b740d75ae743825f244414934b7c014aae/address"
url = "http://localhost:8090:8090/v2/wallets/101b3814d6977de4b58c9dedc67b87c63a4f36dd"

payload={}
headers = {
  'Content-Type': 'application/json'
}

response = requests.delete("GET", url, headers=headers, data=payload).json()

print(response)


## Cardano Developer Portal