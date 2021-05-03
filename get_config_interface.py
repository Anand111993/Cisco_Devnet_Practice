from ncclient import manager
import xmltodict
import xml.dom.minidom
import pprint


 

router = {"host":"sandbox-iosxe-latest-1.cisco.com", "port":830, "username":"developer", "password":"C1sco12345"}

# Create an XML filter for targeted NETCONF queries
netconf_filter = """
 <filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
   </interfaces>
 </filter>"""



with  manager.connect(host=router['host'], port=router['port'], username=router['username'],
                      password=router['password'], hostkey_verify=False) as m:


                      for capability in m.server_capabilities:
                        print(capability)




