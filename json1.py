import urllib.request, urllib.parse, urllib.error
import json

sum1 = 0
url = input("enter the address")
uh = urllib.request.urlopen(url)
data = uh.read().decode()

info = json.loads(data)

for item in info["comments"] :
    value = int(item["count"])
    sum1 = sum1 + value

print(sum1)
