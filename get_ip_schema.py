from ncclient import manager
import xml.etree.ElementTree as ET


router = {"host": "sandbox-iosxe-latest-1.cisco.com", "port":830, "username":"developer", "password":"C1sco12345"}

with manager.connect(host=router['host'], port=router['port'], username=router['username'],
                     password=router['password'], hostkey_verify=False) as m:



                     ip_schema = m.get_schema('ietf-ip')
                     root = ET.fromstring(ip_schema.xml)
                     yang_tree = list(root)[0].text
                     f = open('ietf-ip.yang', 'w')
                     f.write(yang_tree)
                     f.close



