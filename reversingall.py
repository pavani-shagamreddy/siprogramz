#reversing a ll iterative approach

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def reversell(head):
    if(head==None or head.next==None):
        return head
    p=None
    h=head
    while(h!=None):
        t=h.next
        h.next=p
        p=h
        h=t
    return p
def traversal(head):
    if(head==None):
        print("ll is empty")
    else:
        while(head!=None):
            print(head.data,end=" ")
            head=head.next
        print()

l=[1,2,3,4,5,6]
n=6
head=node(1)
temp=head
for i in range(1,n):
    temp.next=node(l[i])
    temp=temp.next
traversal(head)
head=reversell(head)
traversal(head)


