from requests import get

URL = "http://127.0.0.1:5000/api/v1/getcitypollution"

header = {
    "X-Api-Token": "eVDERIPzKkWwQYHwsdZxPxkCnIsGmzSW"
}

response = get(URL, headers=header)
print(response.text)