
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
    
    
    
#🔄 REST API (Meraki Example)

#📜 Script Summary
#Pulls data from the Meraki cloud API about connected clients.

#🔍 Explanation
#REST API: Web-based communication between apps.
#requests.get(): Sends GET request to Meraki API endpoint.
#API key: Authenticates your session.
#.json(): Parses the returned JSON (structured text data).

#You can use this to fetch info from cloud controllers like Meraki, Cisco DNA, Fortinet, etc.