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