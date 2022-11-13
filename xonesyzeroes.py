#generate a number with x 1's and y 0's
x=int(input())
y=int(input())
print(((1<<x)-1)<<y)