import requests

url = "https://cardano-testnet.blockfrost.io/api/v0/epochs/latest"

payload={}
headers = {
  'project_id': 'VVr3ya02i5P9i9hpIlY1stestnethcImSDiPmQ7'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
