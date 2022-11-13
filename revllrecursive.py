class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def revr(head):
    if(head==None or head.next==None):
        return head
    n=revr(head.next)
    head.next.next=head
    head.next=None
    return n
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
head=revr(head)
traversal(head)
