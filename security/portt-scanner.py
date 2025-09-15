import socket

# Target host and ports
target = "192.168.1.1"
ports = [22, 23, 80, 443, 161, 3389]

print(f"🔍 Scanning {target}...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # 1-second timeout
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} is OPEN")
    else:
        print(f"❌ Port {port} is CLOSED")
    sock.close()


#Network Security (Simple Port Scanner)

#📜 Script Summary
#Scans specified TCP ports on a target device and reports which are open/closed.

#🔍 Explanation
#socket: Standard Python library for network connections.
#connect_ex(): Attempts TCP connection; returns 0 if successful.
#ports list: Define which ports you want to check.
#settimeout(): Prevents script from hanging if host doesn’t respond.
#Loop: Iterates through ports and checks connectivity.

#Useful for quick port checks, firewall troubleshooting,
#and verifying if services (SSH, HTTP, SNMP, etc.) are reachable.
