from requests import post

URL = "http://127.0.0.1:5000/api/v1/createblogpost"

data = {
    "title": "Test test test",
    "subtitle": "testino testino testino",
    "creator": "Gioppy"
}

response = post(URL, data=data)
print(response.text)