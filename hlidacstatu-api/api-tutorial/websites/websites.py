import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

# url = Weby
# url = Weby/{id}

response = requestsHSAPI.request('Weby')

print(response.status_code)

if response.status_code == 200:
    jsonParser.writeToJson('data/weby.json', response.json())
