import requests

token = "your_netbox_token"
url = "http://netbox.local/api/dcim/devices/"
headers = {"Authorization": f"Token {token}"}

response = requests.get(url, headers=headers)
devices = response.json()["results"]

for device in devices:
    print(device["name"], "-", device["primary_ip"])