import urllib.request
import re
from bs4 import BeautifulSoup
count=int(input('Enter count'))
position=int(input('Enter Position'))
url=input('Enter the URL')
def links():
    global url
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html5lib')
    link=soup.find_all('a')
    end=link[position-1]
    end=end.get('href',None)
    url=end
    print(end)
    return end
for i in range(count):
    a=links()
    i=i+1
print('\nThe final link in sequence is = ',a)
last_name=re.findall('by_(\S+)\.',a)
print('The Name we want to retreive is',last_name[0])