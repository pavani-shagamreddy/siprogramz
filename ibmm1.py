n=int(input())
if(n<=11):
    print("0")
else:
    c=0
    for i in range(2,(n//6)+1):
        if(n%i==0):
            c+=1
    print(c)

