from netmiko import ConnectHandler
import getpass

device = input('Device IP: ')
username= input('User: ')
password= getpass.getpass()

# for x in range(20,26):

cisco_sw = {
        'device_type': 'cisco_ios',
        'ip': device,
        'username': username,
        'password': password
    }

with open('Config Commands.txt') as f:
    lines = f.read().splitlines()
print (lines)

net_connect = ConnectHandler(**cisco_sw)
output = net_connect.send_config_set(lines)
print (output)

    #for i in range(51,61):
    #    print('Creating Vlan ' + str(i) + " in SW_" + str(x))
    #    config_commands = ['vlan '+ str(i), 'name Python_VLAN ' + str(i)]
    #    output = net_connect.send_config_set(config_commands)
    #    print(output)
