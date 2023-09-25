import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"interface GigabitEthernet 0/0\n")
tn.write(b"ip address 1.1.1.1 255.0.0.0\n")
tn.write(b"no shutdown\n")
tn.write(b"exit\n")
tn.write(b"show ip route\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))