from pysnmp.hlapi import *

# List of devices (IP, community)
devices = [
    ("192.168.1.1", "public"),
    ("192.168.1.2", "public")
]

# OID for system uptime (in hundredths of seconds)
uptime_oid = "1.3.6.1.2.1.1.3.0"

def get_snmp_data(ip, community, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=0),
        UdpTransportTarget((ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
    if errorIndication:
        return None
    elif errorStatus:
        return None
    else:
        for varBind in varBinds:
            return varBind.prettyPrint().split("=")[1].strip()

for ip, community in devices:
    uptime = get_snmp_data(ip, community, uptime_oid)
    if uptime:
        print(f"✅ {ip} uptime: {uptime}")
    else:
        print(f"❌ {ip} SNMP query failed")


#Network Monitoring (SNMP Uptime Check)

#📜 Script Summary
#Polls devices over SNMP and retrieves their system uptime.

#🔍 Explanation
#pysnmp: Python library for SNMP operations.
#CommunityData: SNMP community string for authentication.
#ObjectType(ObjectIdentity()): Defines the OID we want to query.
#uptime OID: 1.3.6.1.2.1.1.3.0 gives system uptime in ticks.
#getCmd(): Sends an SNMP GET request to the device.
#Loop: Prints uptime for each device in the list.

#Useful for monitoring device stability, detecting reboots,
#and integrating SNMP checks into automation workflows.
