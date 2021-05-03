from ncclient import manager
import xmltodict

host = 'sandbox-iosxe-latest-1.cisco.com'
port = 830
username = 'developer'
password = 'C1sco12345' 

m = manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False,
    look_for_keys=False)
                   


SECHEMA = m.get_schema('Cisco-IOS-XE-interfaces')
print(SECHEMA)

m.close_session()



