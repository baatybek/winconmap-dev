import requests
import json


with open('../authorization.json') as auth_token_json:
    data = json.load(auth_token_json)
    token = data['token']
    url_base = data['url_base']

url = url_base + 'dumps'

r = requests.get(url, headers={'Authorization': token})

with open('data/dumps.json', 'w') as dumps_json:
    json.dump(r.json(), dumps_json, indent=4, sort_keys=True)

print(r.status_code)
