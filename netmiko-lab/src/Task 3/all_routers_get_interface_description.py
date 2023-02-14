from netmiko import ConnectHandler 

r1 ={
"device_type": "cisco_ios",
"ip": "192.168.1.101", # R1 Mgmt Interface 
"username": "student", 
"password": "Meilab123",
"port": "22" }

r2 = {
    "device_type": "cisco_ios",
"ip": "192.168.1.102", # R2 Mgmt Interface 
"username": "student", 
"password": "Meilab123",
"port": "22" }

r3 = {
    "device_type": "cisco_ios",
"ip": "192.168.1.103", # R3 Mgmt Interface 
"username": "student", 
"password": "Meilab123",
"port": "22" }

r4 = {
    "device_type": "cisco_ios",
"ip": "192.168.1.104", # R4 Mgmt Interface 
"username": "student", 
"password": "Meilab123",
"port": "22" }

n=1
for device in (r1, r2, r3, r4):
    net_connect = ConnectHandler(**device) 
    output = net_connect.send_command("show interface description") 
    net_connect.disconnect() 
    print(f"For Router {n}")
    print("-"*100) 
    print(output) 
    print("-"*100)
    n +=1