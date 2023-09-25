import getpass
import sys
import telnetlib

for i in range(15,17):
    HOST = "192.168.122."+str(i)
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ")
    tn.write("7m" + "\n")
    tn.write("en\n")
    tn.write("conf t\n")

    for j in range(2,10):

        tn.write("vlan" +str(j) + "\n")

        tn.write("name" "vlan_"+str(j) + "\n")

    tn.write("end\n")
    tn.write("exit\n")
    print(tn.read_all())