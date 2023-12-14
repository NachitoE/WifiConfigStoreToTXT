import xml.etree.ElementTree as ET
import os
import sys

try:
    tree = ET.parse(sys.argv[1])
except IndexError:
    print('File as argument not found.')
    os.system("pause")
    
root = tree.getroot()
network_list = []
file = open("data.txt", 'w')

for x in root.findall('NetworkList/Network/WifiConfiguration'):
    network = {
        "SSID": '',
        "Password": ''
    }
    for j in x.findall('string'):
        if(j.get('name') == 'SSID'):
            network['SSID'] = j.text
        if(j.get('name') == 'PreSharedKey'):
            network['Password'] = j.text
    network_list.append(network)

for x in network_list:
    file.write(f"SSID: {x['SSID']}\nPassword: {x['Password']}\n\n")

print("FILE CREATED!")
os.system("pause")

    