"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
x=max(a,b)
y=min(a,b)
while y:
    x,y=y,x%y
gcd=x
lcm=(a*b)//gcd
print(lcm,gcd)
******************************************************************"""
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
x=max(a,b)
y=min(a,b)
for i in range(1,y+1):
    if(x%i==0 and y%i==0):
        hcf=i
print(hcf)
**************************************************************************"""
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
x=max(a,b)
y=min(a,b)
for i in range(a*b,x-1,-1):
    if(i%x==0 and i%y==0):
        lcm=i
print(lcm)
**************************************************************************"""
"""
recursion:finding lcm using gcd


def gcd(n1,n2):
    if(n1==0):
        return n2
    return gcd(n2%n1,n1)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
g=gcd(a,b)
l=(a*b)//g
print(l,g)
******************************************************************"""
"""

lcm using recursion without finding gcd

def findlcm(n1,n2,k):
    if(k%n1==0 and k%n2==0):
        return k
    return findlcm(n1,n2,k+1)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(findlcm(a,b,max(a,b)))

***********************************************************"""
"""lcm of more than 2 numbers using inbuilt function


from functools import reduce
def gcd(n1,n2):
    if(n1==0):
        return n2
    return gcd(n2%n1,n1)
l=[4,5,6,7]
g=reduce(lambda x,y:(x*y)//gcd(x,y),l)
print(g)

************************************************************"""
"""
lcm of more than 2 numbers without using inbuilt function
 
def gcd(n1,n2):
    if(n1==0):
        return n2
    return gcd(n2%n1,n1)
l=[4,5,6,7]
lcm=l[0]
for i in range(1,len(l)):
    lcm=(l[i]*lcm)//gcd(l[i],lcm)
print(lcm)

**********************************************************************"""