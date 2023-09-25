# #!/usr/bin/env python
# import os
# from netmiko import ConnectHandler
# from getpass import getpass
#
# if os.getenv("NETMIKO_PASSWORD"):
#     password = os.getenv("NETMIKO_PASSWORD")
# else:
#     getpass()
#
# device = {
#     "device_type": "cisco_ios",
#     "host": "cisco1.lasthop.io",
#     "username": "pyclass",
#     "password": "password",
#     "ssh_config_file": "./ssh_config",
# }
#
# with ConnectHandler(**device) as net_connect:
#     output = net_connect.send_command("show users")
#     print(output)
#
#
# *********************
# import sys
# from netmiko import ConnLogOnly
#
# # device dictionary not shown
# conn = ConnLogOnly(**device)
# if conn is None:
#     # Errors will be logged in 'netmiko.log'
#     sys.exit("Logging in failed")
#
# print(conn.find_prompt())
# conn.disconnect()
#
#
# *************************
# import sys
# from netmiko import ConnLogOnly
#
# device1 = {
#     "host": "cisco3.domain.com",
#     "username": "admin",
#     "password": "cisco123",
#     "device_type": "cisco_ios",
# }
#
# conn = ConnLogOnly(**device1)
# if conn is None:
#     sys.exit("Logging in failed")
#
# print("\nWorking case:\n")
# print(conn.find_prompt())
# conn.disconnect()






# from netmiko import ConnectHandler
#
# net_connect = ConnectHandler(
#     device_type="cisco_xe",
#     host="cisco5.domain.com",
#     username="admin",
#     password="password",
# )
#
# output = net_connect.send_command(
#     "show ip arp"
# )
# print(output)