import paramiko

devices = ['192.168.1.1', '192.168.1.2']
username = 'admin'
password = 'yourpassword'

for ip in devices:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('show version')
    print(f"{ip}:\n{stdout.read().decode()}")
    ssh.close()
    
    
    
    #🔐 SSH to Multiple Devices (Paramiko)
    
    #📜 Script Summary
    #Uses SSH connect to multiple devices and run commands like show version.
    
    #🔍 Explanation
    #paramiko: Python SSH client
    #exec_command(): Executes a command on the remote devicec.
    #stdout.read().decode(): Reads the results and decodes bytes to text.
    
    #This is used for inventory collection, verification, or status checks across debices.