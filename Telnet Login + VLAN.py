import getpass
import telnetlib

HOST = input("Enter the remote host IP address: ")
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")

for i in range (3,300):
    tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" + str(i).encode('ascii') + b"\n")
    
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))