from pysnmp.hlapi import *

target = '192.168.1.1'
community = 'public'
oid = '1.3.6.1.2.1.2.2.1.8.1'  # Interface 1 operational status

iterator = getCmd(SnmpEngine(),
                  CommunityData(community),
                  UdpTransportTarget((target, 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity(oid)))

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication:
    print(errorIndication)
else:
    for varBind in varBinds:
        print(f"Status: {varBind}")