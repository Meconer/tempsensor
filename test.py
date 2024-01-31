import requests
from blynkToken import blynkToken


url = "https://fra1.blynk.cloud/external/api/update"

req = requests.get(
    url=url,
    params={"pin": "V0", "value": "28.0", "token": blynkToken},
)

print(req.url)

req = requests.get(
    url=url,
    params={"pin": "V1", "value": "35.0", "token": blynkToken}
)

print(req.url)
