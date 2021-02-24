import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

# url = osoby/{osobaId}
# url = osoby/hledat
# url = osoby/social

response = requestsHSAPI.request('osoby/social')

print(response.status_code)

jsonParser.writeToJson('data/people.json', response.json())
