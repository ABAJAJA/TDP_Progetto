from requests import post

URL = "http://127.0.0.1:5000/api/v1/createMessage"

header = {
    "X-Api-Token": "OrqQfyXOUGIXigjfCHhgTCVNewZWAXEe"
}

data = {
    "name": "nome",
    "email": "email@gmail.com",
    "phone": "123",
    "message": "messaggio di test"
}

response = post(URL, data=data, headers=header)
print(response.text)