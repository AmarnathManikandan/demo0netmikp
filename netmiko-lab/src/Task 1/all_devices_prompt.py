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
    print(f"Default prompt: {net_connect.find_prompt()}")
    net_connect.send_command_timing("disable") 
    print(f"Disable command: {net_connect.find_prompt()}")
    net_connect.send_command_timing("enable") 
    net_connect.send_command_timing("cisco") 
    print(f"Enable command: {net_connect.find_prompt()}")
    print("\n")