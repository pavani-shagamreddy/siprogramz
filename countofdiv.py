n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
print(c)
for i in range(2,c):
    if(c%i==0):
        print("Not prime")
        break
else:
    print("prime")