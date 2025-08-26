from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'yourpassword',
}

net_connect = ConnectHandler(**device)
commands = [
    'hostname Router1',
    'interface Loopback0',
    'ip address 10.0.0.1 255.255.255.0',
    'no shutdown'
]
output = net_connect.send_config_set(commands)
print(output)
net_connect.disconnect()



#⚙️ Network Automation (Netmiko Example)

#📜 Script Summary
#Connects to a Cisco IOS device via SSH and pushes configuration commands.

#🔍 Explanation
#Netmiko: Python library for SSH automation to network devices.
#ConnectHandler: Establishes an SSH session using device details.
#commands list: Contains CLI commands to be applied in config mode.
#send_config_set(): Sends the list of commands as a configuration set.
#disconnect(): Closes the SSH session cleanly.

#This can be used for network automation tasks like bulk configuration, 
#provisioning, or template-based changes across routers/switches.