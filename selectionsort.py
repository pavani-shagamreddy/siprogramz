n=7
l=[10,4,5,6,2,1,2]
for i in range(n-1):
    minn = i
    for j in range(i+1,n):
        if(l[j]<=l[minn]):
            minn=j
    l[i],l[minn]=l[minn],l[i]
print(l)

