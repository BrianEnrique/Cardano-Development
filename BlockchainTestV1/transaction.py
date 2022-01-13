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

balance = transaction_data = {"passphrase": "brianWallets"}

print(">>>", transaction_data)

response = requests.post('http://161.97.114.244:8090/v2/wallets/101b3814d6977de4b58c9dedc67b87c63a4f36dd/balance', json=transaction_data).text

print(response)
print(":.: Complet Tx ADA")






#-------------------------------------------------------------------------------------------------------------------------------------------#

transaction_data = {"passphrase": "brianWallets", "payments": [
  {"address": "addr_test1qrf8043sxgmtm9e5ks4nn9ew0jmkg4mzujvh3xy8rsu923vwcmyw2sqzshu2yjpg39y7ea0au4fxkf26en0ujhh4sx8q3j3n95", 
  "amount": {
    "quantity":2000000, "unit": "lovelace" 
    }
  }]}

print(">>>", transaction_data)

response = requests.post('http://161.97.114.244:8090/v2/wallets/101b3814d6977de4b58c9dedc67b87c63a4f36dd/transactions', json=transaction_data).text
print(response)
print(":.: Complet Tx ADA")

