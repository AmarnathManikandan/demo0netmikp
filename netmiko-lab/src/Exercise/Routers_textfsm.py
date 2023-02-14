from netmiko import Netmiko 
device = {"device_type": "cisco_ios", 
          "ip": "192.168.1.105", 
          "username": "student", 
          "password": "Meilab123", 
          "port": "22"}
net_connect = Netmiko(**device)
output = net_connect.send_command("show ip route", use_textfsm=True) 
net_connect.disconnect() 
print("---------------------Routing Table for R1---------------------")
print("\n")
print("Network"+ "                " + "Next Hop")  
print("\n")
for interface in output: 
    print(interface['network'] + "               " + interface['nexthop_ip'])

device = {"device_type": "cisco_ios", 
          "ip": "192.168.1.102", 
          "username": "student", 
          "password": "Meilab123", 
          "port": "22"}
net_connect = Netmiko(**device)
output = net_connect.send_command("show ip route", use_textfsm=True) 
net_connect.disconnect() 

print("---------------------Routing Table for R2---------------------")
print("\n")
print("Network"+ "                " + "Next Hop")  
print("\n")
for interface in output: 
    print(interface['network'] + "               " + interface['nexthop_ip'])


device = {"device_type": "cisco_ios", 
          "ip": "192.168.1.103", 
          "username": "student", 
          "password": "Meilab123", 
          "port": "22"}
net_connect = Netmiko(**device)
output = net_connect.send_command("show ip route", use_textfsm=True) 
net_connect.disconnect() 

print("---------------------Routing Table for R3---------------------")
print("\n")
print("Network"+ "                " + "Next Hop")  
print("\n")
for interface in output: 
    print(interface['network'] + "               " + interface['nexthop_ip'])

device = {"device_type": "cisco_ios", 
          "ip": "192.168.1.104", 
          "username": "student", 
          "password": "Meilab123", 
          "port": "22"}
net_connect = Netmiko(**device)
output = net_connect.send_command("show ip route", use_textfsm=True) 
net_connect.disconnect() 

print("---------------------Routing Table for R4---------------------")
print("\n")
print("Network"+ "                " + "Next Hop")  
print("\n")
for interface in output: 
    print(interface['network'] + "               " + interface['nexthop_ip'])
