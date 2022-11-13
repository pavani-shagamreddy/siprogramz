class node:
    def __init__(self,data):
        self.data=data
        self.l=self.r=None
def insert(root,key):
    if(root==None):
        return node(key)
    if(key<=root.data):
        root.l=insert(root.l,key)
    else:
        root.r=insert(root.r,key)
    return root
def preorderr(root):
    if(root!=None):
        print(root.data,end=" ")
        preorderr(root.l)
        preorderr(root.r)
def inorderr(root):
    if(root!=None):
        inorderr(root.l)
        print(root.data,end=" ")
        inorderr(root.r)
def postorderr(root):
    if(root!=None):
        postorderr(root.l)
        postorderr(root.r)
        print(root.data, end=" ")
l=[6,9,7,8,10,11,3,2,1]
n=len(l)
rt=None
for i in l:
    rt=insert(rt,i)
preorderr(rt)
print()
inorderr(rt)
print()
postorderr(rt)