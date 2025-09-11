import subprocess
from netmiko import ConnectHandler

# Load device IPs from a file
with open("devices.txt") as f:
    devices = [line.strip() for line in f.readlines()]

for ip in devices:
    print(f"\nChecking {ip}...")
    # Step 1: Ping test
    result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"✅ {ip} is reachable")
        # Step 2: Try SSH connection
        device = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': 'admin',
            'password': 'yourpassword',
        }
        try:
            net_connect = ConnectHandler(**device)
            print(f"🔐 SSH login successful on {ip}")
            net_connect.disconnect()
        except Exception as e:
            print(f"❌ SSH login failed on {ip}: {e}")
    else:
        print(f"❌ {ip} is unreachable")


#Network Automation (Device Reachability Check)

#📜 Script Summary
#Reads device IPs, pings them, and checks SSH accessibility.

#🔍 Explanation
#devices.txt: File containing list of IP addresses (one per line).
#subprocess.run(): Pings the device to test reachability.
#Netmiko ConnectHandler: Attempts SSH login if device responds.
#Exception handling: Catches SSH failures gracefully.
#print(): Shows success/failure for each step.

#Useful for inventory validation, troubleshooting connectivity,
#and quickly verifying which devices are accessible in a network.
