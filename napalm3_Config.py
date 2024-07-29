from napalm import get_network_driver
from napalm.base.exceptions import ConnectionException, CommandErrorException
import getpass
import json
import duo_client

# Duo API credentials
DUO_INTEGRATION_KEY = 'DI9X2DSZVI9HPRUUY3RI'
DUO_SECRET_KEY = 'QPerAWDDLvZWjvcjchomKbDT6v04TM5dKt8lCNaO'
DUO_API_HOSTNAME = 'api-454d04f2.duosecurity.com'

# Initialize Duo client
duo_auth = duo_client.Auth(
    ikey=DUO_INTEGRATION_KEY,
    skey=DUO_SECRET_KEY,
    host=DUO_API_HOSTNAME
)

def duo_2fa(username):
    # Send authentication request to Duo
    auth_response = duo_auth.auth(
        username=username,
        factor='push',
        device='auto'
    )
    
    # Check the response
    if auth_response['result'] == 'allow':
        print("2FA successful")
        return True
    else:
        print("2FA failed")
        return False

cisco_device_ip = input("Input the Cisco's Device IP: ")
username = input("Enter your username: ")
password = getpass.getpass()

# Perform 2FA
if not duo_2fa(username):
    print("Exiting due to failed 2FA")
    exit(1)

# try and except learning

try:

    driver = get_network_driver('ios')
    router = driver(cisco_device_ip, username, password)

    try:
        router.open()
        print("Successfully conneceted to: " + str(cisco_device_ip))

    except (ConnectionException, Exception) as e:
        print("Failed to connect to " + str(cisco_device_ip) + f": {e}" )
        exit(1)
    
    try:
        router.load_merge_candidate(filename='Config Commands AccessSW.txt')
        router.commit_config()
        router.close()

        #print(json.dumps(router_output, indent=4))

        #router_output = router.get_arp_table()
        #print(json.dumps(router_output, sort_keys=True, indent=4))

        #router_output = router.get_interfaces_ip()
        #print(json.dumps(router_output, sort_keys=True, indent=4))
        
    except (ConnectionException, CommandErrorException) as e:
        print("Failed to execute command on " + str(cisco_device_ip) + f": {e}" )
        exit(1)

except Exception as e:
    print(f"An unexpected error ocurred: {e}")
    exit(1)