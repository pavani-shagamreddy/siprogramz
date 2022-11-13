def partition(l,low,high):
    pivot = l[low]
    i=low+1
    j=high
    while True:
        while(i<=j and l[i]<=pivot):
            i+=1
        while(j>=i and l[j]>=pivot):
            j-=1
        if(i<=j):
            l[i],l[j]=l[j],l[i]
        else:
            l[low],l[j]=l[j],l[low]
            return j
def qs(l,low,high):
    if(low<high):
        j=partition(l,low,high)
        qs(l,low,j-1)
        qs(l,j+1,high)
l=[10,4,5,2,2,1]
qs(l,0,5)
print(l)