from requests import post

URL = "http://127.0.0.1:5000/api/v1/createblogpost"

data = {
    "title": "Quanto è inquinata la tua città?",
    "subtitle": "Scopri quanto è inquinata l'aria che respiri",
    "creator": "Gioppy"
}

response = post(URL, data=data)
print(response.text)