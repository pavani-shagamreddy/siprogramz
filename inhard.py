n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
if(len(d)==1):
    print(l[0]*10)
else:
    while(d[l[0]]>1):
        d[l[0]]-=1
        l.pop(0)
    power=[1]
    m=1e9+7
    for i in range(len(l)):
        z=(power[i]*10)%m
        power.append(z)
    ans=0
    for i in range(len(l)):
        ans=(ans+(l[i]*power[i+1])%m)%m
    print(ans)





