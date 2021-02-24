import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

# url = firmy/ico/{ico}
# url = firmy{jmenoFirmy}
# url = firmy/social

response = requestsHSAPI.request('firmy/social')

print(response.status_code)
print(response.json())

jsonParser.writeToJson('data/companies.json', response.json())
