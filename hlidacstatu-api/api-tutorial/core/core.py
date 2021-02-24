import RequestHSAPI
import jsonParser

requestsHSAPI = RequestHSAPI.RequestHSAPI('../authorization.json')

response = requestsHSAPI.request('ping/Hello')
assert 200 == response.status_code
assert 'pong Hello' == response.json()

response = requestsHSAPI.request('getmyip')
assert 200 == response.status_code
print('My ip = ' + response.json())

response = requestsHSAPI.request('dumps')
assert 200 == response.status_code
jsonParser.writeToJson('data/dumps.json', response.json())
