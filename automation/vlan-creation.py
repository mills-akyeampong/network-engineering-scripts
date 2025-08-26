from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.10',
    'username': 'admin',
    'password': 'yourpassword',
}

net_connect = ConnectHandler(**device)
vlans = [10, 20, 30]

for vlan in vlans:
    commands = [f'vlan {vlan}', f'name VLAN_{vlan}']
    output = net_connect.send_config_set(commands)
    print(output)

net_connect.disconnect()



#⚙️ Network Automation (Netmiko VLAN Example)

#📜 Script Summary
#Automates VLAN creation on a Cisco IOS device using SSH.

#🔍 Explanation
#Netmiko: Python library for network device automation.
#ConnectHandler: Establishes SSH session with Cisco IOS device.
#vlans list: VLAN IDs to be created.
#Loop: Iterates through VLAN IDs and builds configuration commands.
#send_config_set(): Sends VLAN creation commands to the device.
#disconnect(): Ends the SSH session.

#make sure you have netmiko installed: pip install netmiko
#Useful for automating switch provisioning, ensuring consistent VLAN 
#deployments, and reducing manual CLI configuration errors.