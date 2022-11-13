def ms(l,low,mid,high):
    p1=low
    p2=mid+1
    c=[0]*(high-low+1)
    t=0
    while(p1<=mid and p2<=high):
        if(l[p1]<l[p2]):
            c[t]=l[p1]
            t+=1
            p1+=1
        else:
            c[t]=l[p2]
            t+=1
            p2+=1
    while(p1<=mid):
        c[t]=l[p1]
        t+=1
        p1+=1
    while(p2<=high):
        c[t]=l[p2]
        t+=1
        p2+=1
    for i in range(low,high+1):
        l[i]=c[i-low]
def merge(l,low,high):
    if(low==high):
        return
    mid=(low+high)//2
    merge(l,low,mid)
    merge(l,mid+1,high)
    ms(l,low,mid,high)
l=[10,4,5,6,2,1,2]
merge(l,0,6)
print(l)
