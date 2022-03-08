import requests
import os

url = requests.get("http://cadmin@prod.hclpnp.com:Pa88w0rd@travelmysql1.iris.cwp.pnp-hcl.com/traveler")
htmltext = url.text

f=open("url.txt","w")
f.write(htmltext)
f.close()

f=open("url.txt","r")
s=f.read()
Start_Traveller =s.find('Traveler Version:')+len('Traveler Version:')
End_Traveller=s.find('</span><br role="presentation"/><span role="presentation">')
substring=s[Start_Traveller:End_Traveller]
print("Traveller Version :-",substring)

start_Domino = s.find('Domino Version:') + len('Domino Version:')
end_Domino = s.find('</span><br role="presentation"/>External')
substring1 = s[start_Domino:end_Domino]
print("Domino version :- ",substring1)

f.close()
os.remove('url.txt')
