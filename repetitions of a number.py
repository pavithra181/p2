x,y=map(int,input().split())
l=list(map(int,input().split()))
count=0
for j in l:
	if(j==y):
		count=count+1
print(count)
