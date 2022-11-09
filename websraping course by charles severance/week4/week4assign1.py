import urllib.request
from bs4 import BeautifulSoup

sum=0
url = 'https://py4e-data.dr-chuck.net/comments_1670866.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html5lib')
tag = soup('span')
for tags in tag:
    total = tags.text
    total=int(total)
    sum=sum+total
print(sum)


