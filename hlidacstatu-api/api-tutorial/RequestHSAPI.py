import jsonParser
import requests

class RequestHSAPI:
    
authorization = jsonParser.readFromJson('../authorization.json')
token = authorization['token']
url_base = authorization['url_base']


def request(url):
    return requests.get(url_base + url, headers={'Authorization': token})


def requestWithHeader(url, headers):
    return requests.get(url_base + url, headers)
