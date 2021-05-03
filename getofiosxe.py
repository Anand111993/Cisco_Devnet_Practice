from ncclient import manager

import xmltodict

host = 'sandbox-iosxe-latest-1.cisco.com'
port = 830
username = 'developer'
password = 'C1sco12345'


get_rply = manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False,
    look_for_keys=False)


for rply in get_rply.server_capabilities:
    print(rply)

get_rply.close_session()