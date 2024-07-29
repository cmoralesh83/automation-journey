from netmiko import ConnectHandler
import getpass

router = input('Router IP address: ')
core_sw = input('Core Switch IP: ')
username= input('User: ')
password= getpass.getpass()

# Configuring Access Switches

print('Configuring Access Switches... Please Wait!')

for x in range(22,26):
    
    device = '192.168.100.' + str(x)

    cisco_access_sw = {
            'device_type': 'cisco_ios',
            'ip': device,
            'username': username,
            'password': password
        }

    with open('Config Commands AccessSW.txt') as f:
        lines = f.read().splitlines()
    
    net_connect = ConnectHandler(**cisco_access_sw)
    
    try:
        output = net_connect.send_config_set(lines, read_timeout=100)  # Increase read_timeout
        output2 = net_connect.send_command('write memory')
        print(output + output2)
    except Exception as e:
        print(f"Error configuring device {device}: {e}")

# Configuring Core Switch

print('Access Switches Configured.... Initiating Switch Core Configuration... Please Wait')

cisco_access_sw = {
    'device_type': 'cisco_ios',
    'ip': core_sw,
    'username': username,
    'password': password
    }

with open('Config Commands CoreSW.txt') as f:
    lines = f.read().splitlines()
    
net_connect = ConnectHandler(**cisco_access_sw)
    
output = net_connect.send_config_set(lines)
output2 = net_connect.send_command('write memory')
print(output + output2)

# Configuring Core Switch

print('Core Switch Configured.... Initiating Switch Core Configuration... Please Wait')

cisco_router = {
    'device_type': 'cisco_ios',
    'ip': router,
    'username': username,
    'password': password
    }

with open('Config Commands CoreRo.txt') as f:
    lines = f.read().splitlines()
    
net_connect = ConnectHandler(**cisco_router)
    
output = net_connect.send_config_set(lines)
print(output)