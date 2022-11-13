l=[]
for i in range(3,101):
    if(i%3==0 or i%7==0):
        l.append(i)
t=int(input())
n=len(l)
for i in range(t):
    k=int(input())
    if k in l:
        print("True")
    else:
        p1=0
        p2=n-1
        while(p1<p2):
            s=l[p1]+l[p2]
            if(s>k):
                p2-=1
            elif(s<k):
                p1+=1
            else:
                print("TRUE")
                break
        else:
            print("FALSE")



