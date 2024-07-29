from netmiko import ConnectHandler
import getpass

username= input('User: ')
password= getpass.getpass()

for x in range(20,26):

    cisco_sw = {
        'device_type': 'cisco_ios',
        'ip': '192.168.100.' + str(x),
        'username': username,
        'password': password
    }

    net_connect = ConnectHandler(**cisco_sw)
    output = net_connect.send_command('write memory')
    print (output)

    #for i in range(51,61):
    #    print('Creating Vlan ' + str(i) + " in SW_" + str(x))
    #    config_commands = ['vlan '+ str(i), 'name Python_VLAN ' + str(i)]
    #    output = net_connect.send_config_set(config_commands)
    #    print(output)



