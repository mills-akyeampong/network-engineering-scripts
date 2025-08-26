import requests

token = "your_netbox_token"
url = "http://netbox.local/api/dcim/devices/"
headers = {"Authorization": f"Token {token}"}

response = requests.get(url, headers=headers)
devices = response.json()["results"]

for device in devices:
    print(device["name"], "-", device["primary_ip"])
    
    
    
#🔄 REST API (NetBox Example)

#📜 Script Summary
#Pulls a list of devices from a NetBox instance via its REST API.

#🔍 Explanation
#REST API: Standard way apps exchange data over HTTP.
#requests.get(): Sends GET request to the NetBox devices endpoint.
#Token: Authenticates your session (provided in headers).
#.json(): Parses the JSON response into Python objects.
#results: NetBox paginates data; "results" contains the actual devices list.

#You can use this to fetch inventory details from NetBox and integrate it 
#with automation workflows (e.g., Ansible, Nornir, custom Python scripts).