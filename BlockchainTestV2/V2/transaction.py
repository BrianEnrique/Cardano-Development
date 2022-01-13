import requests
import json

url = "http://161.97.114.244:8090/v2/wallets"

payload={}
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=payload).json()

print(response)

#-------------------------------------------------------------------------------------------------------------------------------------------#

transaction_data = {"passphrase": "brianWalletsLocalv2", "payments": [
  {"address": "addr_test1qr6zuu3ar4susllkpmgnfj84mfsmdzg3sndkxnm4dttnkh5wcmyw2sqzshu2yjpg39y7ea0au4fxkf26en0ujhh4sx8q8z8p0y", 
  "amount": {
    "quantity":1000000, "unit": "lovelace" 
    }
  }]}

print(">>>", transaction_data)

response = requests.post('http://161.97.114.244:8090/v2/wallets/101b3814d6977de4b58c9dedc67b87c63a4f36dd/transactions', json=transaction_data).text
print(response)
print(":.: Complet Tx ADA")

