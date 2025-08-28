from netmiko import ConnectHandler
from datetime import datetime

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'yourpassword',
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command('show running-config')

now = datetime.now().strftime("%Y%m%d_%H%M%S")
with open(f'backup_{now}.txt', 'w') as f:
    f.write(output)

net_connect.disconnect()


#🔄 Network Automation (Netmiko Backup Example)

#📜 Script Summary
#Connects to a Cisco IOS device via SSH, retrieves the running-config, 
#and saves it to a timestamped backup file.

#🔍 Explanation
#Netmiko: Python library to automate SSH connections.
#ConnectHandler: Opens an SSH session with device credentials.
#send_command(): Executes "show running-config" and captures output.
#datetime: Generates unique timestamp for the backup filename.
#open/write: Creates a text file and writes configuration data.
#disconnect(): Closes the SSH session cleanly.

#Useful for automated config backups, compliance checks, and 
#disaster recovery planning in network operations