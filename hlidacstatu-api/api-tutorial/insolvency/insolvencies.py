import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

# url = insolvence/hledat
# url = insolvence/hledat/{id}

response = requestsHSAPI.request('insolvence/hledat')

print(response.status_code)

if response.status_code == 200:
    jsonParser.writeToJson('data/insolvence.json', response.json())
