n=len(s)
c=[0]*n
c[0]=s[0]
ans=[]
for i in range(1,n):
    c[i]=c[i-1]+s[i]
for i in range(n-1):
    f1=c[i]
    f2=c[n-1]-c[i]
    m=abs((f1//(i+1))-(f2//(n-1-i)))
    ans.append(m)
minn=min(ans)
for i in range(len(ans)):
    if(ans[i]==minn):
        return i+1


