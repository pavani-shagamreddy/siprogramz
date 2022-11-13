#count the total set bits of given number N
""""
n=int(input())
c=0
for i in range(32):
    if(n&(1<<i)):
        c+=1
print(c)
 *****************************************************************************"""
"""
c=0
n=int(input())
while(n!=0):
    if(n&1):
        c+=1
    n=n>>1
print(c)
***************************************************"""
c=0
n=int(input())
while(n!=0):
    n=n&(n-1)
    c+=1
print(c)
