from napalm import get_network_driver
from napalm.base.exceptions import ConnectionException, CommandErrorException
import getpass
import json

cisco_device_ip = input("Input the Cisco's Device IP: ")
username = input("Enter your username: ")
password = getpass.getpass()

# try and except learning

try:

    driver = get_network_driver('ios')
    router = driver(cisco_device_ip, username, password)

    try:
        router.open()
    except (ConnectionException, Exception) as e:
        print("Failed to connect to " + str(cisco_device_ip) + f": {e}" )
        exit(1)
    
    try:
        router_output = router.get_mac_address_table()
        print(json.dumps(router_output, indent=4))

        router_output = router.get_arp_table()
        print(json.dumps(router_output, sort_keys=True, indent=4))

        #router_output = router.get_interfaces_ip()
        #print(json.dumps(router_output, sort_keys=True, indent=4))
        
    except (ConnectionException, CommandErrorException) as e:
        print("Failed to execute command on " + str(cisco_device_ip) + f": {e}" )
        exit(1)

except Exception as e:
    print(f"An unexpected error ocurred: {e}")
    exit(1)


