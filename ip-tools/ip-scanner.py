import subprocess

for i in range(1, 255):
    ip = f"192.168.1.{i}"
    result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL)
    if result.returncode != 0:
        print(f"{ip} is available")


#Network Utility (Ping Sweep Example)

#📜 Script Summary
#Scans a subnet (192.168.1.0/24) to check which IP addresses are available.

#🔍 Explanation
#subprocess.run(): Executes system commands from Python.
#ping -c 1: Sends 1 ICMP echo request.
#-W 1: Sets timeout of 1 second.
#stdout=subprocess.DEVNULL: Hides command output for cleaner results.
#returncode: 0 = reply received (host is alive), non-0 = no reply (available).

#Useful for quick network discovery, checking free IP addresses, or 
#building simple inventory/monitoring scripts.
