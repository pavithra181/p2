x,y=map(int,input().split())
l=list(map(int,input().split()))
for j in l:
	if(j==y):
		print("yes")
		break
else:
	print("no")
