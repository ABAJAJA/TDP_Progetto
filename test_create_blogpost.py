from requests import post

URL = "http://127.0.0.1:5000/api/v1/createblogpost"

data = {
    "title": "Hello World",
    "subtitle": "This is a test blog post",
    "creator": "gioppy"
}

response = post(URL, data=data)
print(response.text)
