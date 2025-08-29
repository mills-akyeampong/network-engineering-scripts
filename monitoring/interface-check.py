from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'yourpassword',
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show ip interface brief")
print(output)
net_connect.disconnect()