import json


def writeToJson(path, jsonObject):
    with open(path, 'w') as jsonWriter:
        json.dump(jsonObject, jsonWriter, indent=4, sort_keys=True)


def readFromJson(path):
    with open(path) as jsonReader:
        return json.load(jsonReader)
