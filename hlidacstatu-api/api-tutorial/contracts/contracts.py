import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

# url = smlouvy/hledat
# url = smlouvy/{id}
# url = smlouvy/vsechnaId
# url = smlouvy/text/{id}

response = requestsHSAPI.request('smlouvy/vsechnaId')

print(response.status_code)

if response.status_code == 200:
    jsonParser.writeToJson('data/contracts.json', response.json())
