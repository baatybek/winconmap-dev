import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

# url = datasety
# url = datasety/{datasetId}
# url = datasety/{datasetId}/hledat
# url = datasety/{datasetId}/zaznamy/{itemid}
# url = datasety/{datasetId}/zaznamy/{itemId}/existuje

response = requestsHSAPI.request('datasety')
assert 200 == response.status_code
jsonParser.writeToJson('data/datasets.json', response.json())
