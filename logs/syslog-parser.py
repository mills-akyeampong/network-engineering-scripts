import re

with open('syslog.log', 'r') as file:
    for line in file:
        if re.search(r'%LINK-3-UPDOWN', line):
            print("ALERT:", line.strip())


#Log Monitoring (Syslog Alert Example)

#📜 Script Summary
#Parses a syslog file and triggers an alert when an interface up/down event is detected.

#🔍 Explanation
#re.search(): Uses regex to find patterns in each line.
#%LINK-3-UPDOWN: Cisco syslog message for interface status changes.
#open('syslog.log'): Reads the syslog file line by line.
#line.strip(): Cleans whitespace/newlines before printing.
#print("ALERT"): Displays matching events as alerts.

#Useful for monitoring syslog files, detecting critical events, 
#and integrating with automation scripts for notifications.
