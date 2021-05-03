from ncclient import manager
import xmltodict
import xml.etree.ElementTree as ET

host = 'sandbox-iosxe-latest-1.cisco.com'
port = 830
username = 'developer'
password = 'C1sco12345' 

m = manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False,
    look_for_keys=False)


get_conf = m.get_config(source = 'running')

#get_rply = xmltodict.parse(get_conf.xml)

get_rply = ET.fromstring(get_conf.xml)

running_config = list(get_rply)

print(running_config)

#running_config = list(get_rply)[0].text
#print(get_rply['rpc-reply'])

#f = open('running-config.xml', 'w')

#f.write(running_config)
#f.close


#print(xml.dom.minidom.parseString(get_conf.xml).toprettyxml())


