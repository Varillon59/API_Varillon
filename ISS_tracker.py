import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")


if response.status_code == 200:
    print("Success.")
else:
    print("An error has occurred.")

iss=response.json()

Longitude=iss['iss_position']['longitude']
Latitude=iss['iss_position']['latitude']

print("L'ISS se trouve au coordonnées:", Longitude, "/", Latitude)
