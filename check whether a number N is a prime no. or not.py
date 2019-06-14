f=int(input())
if(f>1):
    for w in range(2,f):
        if(f%w==0):
            print("no")
            break
    else:
    	print("yes")
else:
    print("no")
