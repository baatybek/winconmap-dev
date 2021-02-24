import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

# url = internalq/Voice2TextGetTask

response = requestsHSAPI.request('internalq/Voice2TextGetTask')

print(response.status_code)

if response.status_code == 200:
    jsonParser.writeToJson('data/voice_to_text.json', response.json())
