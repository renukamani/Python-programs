import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
sum = 0
url = input("enter the address")
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for count in counts :
    value = int(count.text)
    sum = sum + value
print(sum)
