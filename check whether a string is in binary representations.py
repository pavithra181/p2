h=input()
a=0
for j in h:
	if(j=='1' or j=='0'):
		a=a+1
if(a==len(h)):
	print("yes")
else:
	print("no")
	
