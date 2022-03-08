import requests
import os


os.remove("url1.txt")
url = requests.get("http://cadmin%40prod.hclpnp.com:Pa88w0rd@travelmysql1.iris.cwp.pnp-hcl.com/api/traveler/devices")
htmltext = url.text

f=open("url1.txt","w")
f.write(htmltext)
f.close()

f=open("url1.txt","r")
lines=f.readlines()
for line in lines :
    if '"code":' in line :
        print(line)

