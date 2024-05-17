from requests import post

URL = "http://127.0.0.1:5000/api/v1/createblogpost"

header = { "X-Api-Token": "SJPTjZSxUWGGTUTGVUDoteNOPNRCdHsS" }

data = {
    "title": "L'inquinamento ai giorni nostri",
    "subtitle": "Scopri di più sull'inquinamento"
}

response = post(URL, data=data, headers=header)
print(response.text)