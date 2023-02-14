from netmiko import Netmiko 

devices =[{
"device_type": "cisco_ios",
"ip": "192.168.1.101", # R1 Mgmt Interface 
"username": "student", 
"password": "Meilab123",
"port": "22" },
{
    "device_type": "cisco_ios",
"ip": "192.168.1.102", # R2 Mgmt Interface 
"username": "student", 
"password": "Meilab123",
"port": "22" },
{
    "device_type": "cisco_ios",
"ip": "192.168.1.103", # R3 Mgmt Interface 
"username": "student", 
"password": "Meilab123",
"port": "22"},
{
    "device_type": "cisco_ios",
"ip": "192.168.1.104", # R4 Mgmt Interface 
"username": "student", 
"password": "Meilab123",
"port": "22", }]

for device in devices:
    net_connect = Netmiko(**device) 
    output = net_connect.send_command("show version") 
    net_connect.disconnect() 
    result = output.find('Configuration register is') 
    begin = int(result) + 25
    end = begin + 38 
    print("Configuration register for " + device['ip'] + " is"+ output[int(begin):int(end)])