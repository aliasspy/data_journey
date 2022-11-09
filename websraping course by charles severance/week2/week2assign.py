import re
numlist=list()
with open('numbers.txt','r') as data:
	for line in data:
		num=re.findall('[0-9]+',line)
		
		for i in num:
			num=float(i)
			numlist.append(num)
	print(numlist)
	totsum=sum(numlist)
	print(totsum)
