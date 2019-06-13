x=input()
d=0
c=0
for w in x:
    if(w.isalpha()==True):
        c=c+1
    elif(w.isdigit()==True):
        d=d+1
if(c>0 and d>0):
    print("Yes")
else:
    print("No")
