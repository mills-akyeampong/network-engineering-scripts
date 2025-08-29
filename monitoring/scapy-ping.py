from scapy.all import IP, ICMP, send

packet = IP(dst="192.168.1.1")/ICMP()
send(packet, count=5)