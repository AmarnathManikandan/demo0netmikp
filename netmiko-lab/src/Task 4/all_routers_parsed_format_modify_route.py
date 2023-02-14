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

n=1 

for device in devices:
    net_connect = Netmiko(**device) 
    output = net_connect.send_command("show ip route", use_textfsm=True)
    net_connect.disconnect() 
    print(f"For Router {n}")
    print("-"*100) 
    print(type(output))
    print("******Protocol******")
    for route in output: 
        print(route['protocol'])
    print("-"*50) 
    print("******Network******")
    for route in output: 
        print(route['network'])
    print("\n")
    print("-"*50) 
    print("******Distance******")
    for route in output: 
        print(route['distance'])
    print("\n")
    print("-"*50) 
    print("******Metric******")
    for route in output: 
        print(route['metric'])
    print("\n")
    n +=1

