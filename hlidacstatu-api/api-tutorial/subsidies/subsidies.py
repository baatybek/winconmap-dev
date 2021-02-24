import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

# url = dotace/hledat
# url = dotace/{id}
response = requestsHSAPI.request('dotace/hledat')

print(response.status_code)
print(response.json())