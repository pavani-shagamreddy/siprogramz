n=int(input())
c=0
for i in range(1,int(n**0.5)+1):
    if(n%i==0):
        c+=2
    if(i*i==n):
        c-=1
print(c)
