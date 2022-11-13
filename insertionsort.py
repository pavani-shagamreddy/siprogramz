n=7
l=[10,4,5,6,2,1,2]
for i in range(1,n):
    temp=l[i]
    j=i-1
    while(j>=0 and l[j]>temp):
        l[j+1]=l[j]
        j-=1
    l[j+1]=temp
print(l)
