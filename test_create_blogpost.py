from requests import post

URL = "http://127.0.0.1:5000/api/v1/createblogpost"

header = {
    "X-Api-Token": "HEgDYgAaUjzphCOsiBVdxmUaBORGEvNn"
}

data = {
    "title": "Test test test",
    "subtitle": "testino testino testino"
}

response = post(URL, data=data, headers=header)
print(response.text)