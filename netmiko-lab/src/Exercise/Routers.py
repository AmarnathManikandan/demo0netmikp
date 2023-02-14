import yaml 
from jinja2 import Environment, FileSystemLoader 
from netmiko import Netmiko
import logging

hosts = yaml.load(open('R1H.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('R1.yml'), Loader=yaml.SafeLoader)

env = Environment(loader = FileSystemLoader('.'), trim_blocks=True, autoescape=True)
template = env.get_template('R1.j2')
loopback_config = template.render(data=interfaces)

for host in hosts["hosts"]:
    net_connect = Netmiko(host = host["name"],
                          username = host["username"],
                          password = host["password"],
                          port = host["port"], 
                          device_type = host["type"])

    
    print(f"Logged into {host['name']} successfully")
    output = net_connect.send_config_set(loopback_config.split("\n"))
    print(f"Pushed config into router R1 --- {host['name']} successfully") 
    net_connect.disconnect()

hosts = yaml.load(open('R2H.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('R2.yml'), Loader=yaml.SafeLoader)

env = Environment(loader = FileSystemLoader('.'), trim_blocks=True, autoescape=True)
template = env.get_template('R2.j2')
loopback_config = template.render(data=interfaces)

for host in hosts["hosts"]:
    net_connect = Netmiko(host = host["name"],
                          username = host["username"],
                          password = host["password"],
                          port = host["port"], 
                          device_type = host["type"])

    
    print(f"Logged into {host['name']} successfully")
    output = net_connect.send_config_set(loopback_config.split("\n"))
    print(f"Pushed config into router R2 --- {host['name']} successfully") 
    net_connect.disconnect()

hosts = yaml.load(open('R3H.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('R3.yml'), Loader=yaml.SafeLoader)

env = Environment(loader = FileSystemLoader('.'), trim_blocks=True, autoescape=True)
template = env.get_template('R3.j2')
loopback_config = template.render(data=interfaces)

for host in hosts["hosts"]:
    net_connect = Netmiko(host = host["name"],
                          username = host["username"],
                          password = host["password"],
                          port = host["port"], 
                          device_type = host["type"])

    
    print(f"Logged into {host['name']} successfully")
    output = net_connect.send_config_set(loopback_config.split("\n"))
    print(f"Pushed config into router R3 --- {host['name']} successfully") 
    net_connect.disconnect()


hosts = yaml.load(open('R4H.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('R4.yml'), Loader=yaml.SafeLoader)

env = Environment(loader = FileSystemLoader('.'), trim_blocks=True, autoescape=True)
template = env.get_template('R4.j2')
loopback_config = template.render(data=interfaces)

for host in hosts["hosts"]:
    net_connect = Netmiko(host = host["name"],
                          username = host["username"],
                          password = host["password"],
                          port = host["port"], 
                          device_type = host["type"])


    print(f"Logged into {host['name']} successfully")
    output = net_connect.send_config_set(loopback_config.split("\n"))
    print(f"Pushed config into router R4 --- {host['name']} successfully") 
    net_connect.disconnect()


logging.basicConfig(filename='Routers.log',
                    filemode='w',
                    datefmt='%d-%b-%y %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')