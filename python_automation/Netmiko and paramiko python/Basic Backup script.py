#!usr/bin/env python

import getpass
import telnetlib

user = input("Enter your telnet username:")

password = getpass.getpass()

f =open("switch_list")

for line in f:
    print("getting backup from switch" + (line))

    HOST = line.strip()

    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")

    tn.write("user", + "\n")

    tn.read_until("Password: ")

    tn.write(password + "\n")

    tn.write("en\n")

    tn.write("ccna\n")

    tn.write("terminal length0\n")

    tn.write("shclock \n")

    tn.write("shrun \n")

    tn.write("exit\n")

    readoutput = tn.read_all()

    saveoutput = open("switch"+HOST,"w")

    saveoutput.write(readoutput)

    saveoutput.close()