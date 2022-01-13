import requests

data = {
    'name'                  :   'brianWalletsLocalv2',
    'mnemonic_sentence'     :  ["expose", "biology", "will", "pause", "taxi", "behave", "inquiry", "lock", "matter", "pride", "divorce", "model", "little", "easily", "solid", "need", "dose", "sadness", "kitchen", "pyramid", "erosion", "shoulder", "double", "fragile"],
    'passphrase'            :   'brianWalletsLocalv2'
}

r = requests.post("http://localhost:8090/v2/wallets", json=data)
#r = requests.post("http://161.97.114.244:8090/v2/wallets", json=data)