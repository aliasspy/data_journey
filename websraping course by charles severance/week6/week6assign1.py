import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0
url='https://py4e-data.dr-chuck.net/comments_1670869.json'
print('Retrieving: ',url)
#Add .read() while creating handle only. json will not parse it if .read() is not done. I always forget this
handle=urllib.request.urlopen(url,context=ctx).read()
js=json.loads(handle)
comment=js['comments']
for i in comment:
    num=int(i['count'])
    sum=sum+num
print(sum)