from ncclient import manager
import xmltodict
import xml.dom.minidom
import pprint


host = 'sandbox-iosxe-latest-1.cisco.com'
port = 830
username = 'developer'
password = 'C1sco12345' 


netconf_filter = """
<filter>
  <native
	xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	<hostname></hostname>
  </native>  
</filter>"""

m = manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False,
    look_for_keys=False)



print(m.get_config('running', netconf_filter))

#data = xmltodict.parse(netconf_rply.xml)

#rint(xml.dom.minidom.parseString(netconf_rply.xml).toprettyxml())

m.close_session()




