

def dec(func):
    def inner(a,b):
        if(b==0):
            print("cant divide")
        else:
            return func(a,b)
    return inner
"""k=dec(div(3,2))"""
@dec
def div(a,b):
    print(a/b)
div(10,10)