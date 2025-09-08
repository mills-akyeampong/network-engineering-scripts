from scapy.all import ARP, Ether, srp

# Define the target subnet
target_ip = "192.168.1.0/24"

# Create ARP request packet
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

# Send the packet and capture responses
result = srp(packet, timeout=2, verbose=0)[0]

print("Available devices in the network:")
print("IP Address\t\tMAC Address")

for sent, received in result:
    print(f"{received.psrc}\t\t{received.hwsrc}")
    

#🔄 Network Discovery (Scapy ARP Scan Example)

#📜 Script Summary
#Discovers all active devices in a subnet by sending ARP requests.

#🔍 Explanation
#Scapy: Powerful Python library for packet crafting/sniffing.
#ARP: Protocol used to map IP addresses to MAC addresses.
#Ether(): Creates an Ethernet broadcast frame.
#srp(): Sends packets at Layer 2 and receives responses.
#Loop: Prints IP and MAC of all responding devices.

#Useful for network mapping, device inventory, and detecting unknown hosts.
