import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

totnum=list()
url='https://py4e-data.dr-chuck.net/comments_1670868.xml'
file=urllib.request.urlopen(url,context=ctx).read()
tree=ET.fromstring(file)
comment=tree.findall('comments/comment')
for i in comment:
    num=i.find('count').text
    intnum=int(num)
    totnum.append(intnum)
sum=sum(totnum)
print(totnum)
print(sum)
