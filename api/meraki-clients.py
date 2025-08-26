
import requests

headers = {
    'X-Cisco-Meraki-API-Key': 'your_api_key',
    'Content-Type': 'application/json',
}

network_id = 'N_1234567890'
url = f'https://api.meraki.com/api/v1/networks/{network_id}/clients'

response = requests.get(url, headers=headers)
clients = response.json()
for client in clients:
    print(client['description'], client['ip'])