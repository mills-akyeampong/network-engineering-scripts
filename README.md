# network-engineering-scripts

A curated collection of useful scripts for network engineers to automate configuration, monitoring, logging, and API integration.

## 🔧 Categories

- `automation/` - VLANs, push config, etc.
- `monitoring/` - Interface status, SNMP, ping sweep, Scapy
- `backups/` - Daily config backup script
- `logs/` - Syslog parsing
- `alerts/` - Email alerts on failure
- `api/` - REST API (NetBox, Meraki)
- `ssh/` - SSH to multiple devices
- `ip_tools/` - IP address availability scanner

## ✅ Requirements

- Python 3.x
- pip install: `netmiko`, `paramiko`, `requests`, `pysnmp`, `scapy`

## Key Concepts Recap

| Script Function  | Language      | Tools/Libraries      |
| ---------------- | ------------- | -------------------- |
| Config Push      | Python        | Netmiko              |
| Ping Sweep       | Bash          | Native utilities     |
| SNMP Polling     | Python        | pysnmp               |
| Email Alerts     | Python        | smtplib, MIME        |
| Log Parsing      | Python        | re (Regex)           |
| IP Scanner       | Python/Bash   | subprocess, ping     |
| SSH to Devices   | Python        | Paramiko             |
| API Calls        | Python        | requests, REST API   |
| VLAN Automation  | Python        | Netmiko              |
| Interface Check  | Python        | Netmiko              |
| Packet Crafting  | Python        | Scapy                |
| Device Inventory | Python        | requests, NetBox API |
| Config Backup    | Python + Cron | datetime, Netmiko    |

## ⚠️ Security Tip

Never hardcode passwords or API keys. Use environment variables or a `.env` file.

## 🧑‍💻 Author

Created by Mills Kojo Akyeampong – Security Systems & Network Engineer.
