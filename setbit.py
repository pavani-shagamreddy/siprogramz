#find ith bit of N is set or not
n=int(input())
i=int(input())
if(n&(1<<i)):
    print("set")
else:
    print("not set")