b=input()
n=len(b)
l=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101"]
if(n%4==0):
    i=0
    r=[]
    while(i<n):
        r.append(str(l.index(b[i:i+4])))
        i+=4
    op=0
    for i in range(len(r)):
        if(r[i]=='10' or r[i]=='11' or r[i]=='12' or r[i]=='13'):
            op=i
    f="".join(r[:op])
    s="".join(r[op+1:])
    if(r[op]=='10'):
        print(int(f)+int(s))
    elif(r[op]=='11'):
        print(int(f) - int(s))
    elif (r[op] == '12'):
        print(int(f) * int(s))
    elif (r[op] == '13'):
        print(int(f) // int(s))
    else:
        print("invalid")
else:
    print("invalid")

