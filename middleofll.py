#find middle element of linkedlist
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def mll(head):
    if(head==None or head.next==None):
        return head
    fast=s=head
    while(fast.next!=None and fast.next.next!=None):
        fast=fast.next.next
        s=s.next
    if(fast.next!=None):
        return s.next
    return s
def traversal(head):
    if(head==None):
        print("ll is empty")
    else:
        while(head!=None):
            print(head.data,end=" ")
            head=head.next
        print()
l=[1,2,3,4,5,6]
n=len(l)
head=node(1)
temp=head
for i in range(1,n):
    temp.next=node(l[i])
    temp=temp.next
traversal(head)
mid=mll(head)
print(mid.data)

