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