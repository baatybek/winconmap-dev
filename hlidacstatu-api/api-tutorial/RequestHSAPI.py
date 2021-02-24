import jsonParser
import requests


class RequestHSAPI:
    def __init__(self, path_to_auth_json):
        self.authorization = jsonParser.readFromJson(path_to_auth_json)
        self.token = self.authorization['token']
        self.url_base = self.authorization['url_base']

    def request(self, url):
        return requests.get(self.url_base + url, headers={'Authorization': self.token})

    def requestWithHeader(self, url, headers):
        return requests.get(self.url_base + url, headers)
