k=int(input())
n=int(input())
f=0
l=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if(i!=j and (l[i]+k)==l[j]):
            f=1
            print(l[i],l[j])
if(f==0):
    print("no such pairs exist")

