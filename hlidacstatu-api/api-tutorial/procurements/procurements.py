import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

# url = /verejnezakazky/{id}
# url = /verejnezakazky/hledat

response = requestsHSAPI.request('smlouvy/vsechnaId')

print(response.status_code)

if response.status_code == 200:
    jsonParser.writeToJson('data/procurements.json', response.json())
