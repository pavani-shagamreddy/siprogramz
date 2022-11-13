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
def levelorderr(root):
    q=[root,None]
    while(q):
        temp=q.pop(0)
        if(temp==None):
            if(q):
                print()
                q.append(None)
        else:
            print(temp.data,end=" ")
            if temp.l:
                q.append(temp.l)
            if temp.r:
                q.append(temp.r)
def levelorder2(root):
    q1=[root]
    q2=[]
    while(q1 or q2):
        while(q1):
            temp=q1.pop(0)
            print(temp.data,end=" ")
            if temp.l:
                q2.append(temp.l)
            if temp.r:
                q2.append(temp.r)
        print()
        while(q2):
            temp=q2.pop(0)
            print(temp.data, end=" ")
            if temp.l:
                q1.append(temp.l)
            if temp.r:
                q1.append(temp.r)
        print()

l=[6,9,7,8,10,11,3,2,1]
n=len(l)
rt=None
for i in l:
    rt=insert(rt,i)
levelorderr(rt)
print()
levelorder2(rt)