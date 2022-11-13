def fun(n):
    yield 2
    yield 3
k=fun(2)
print(k)
print(next(k))
print(next(k))