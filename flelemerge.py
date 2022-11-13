class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def findmid(head):
    if(head==None):
        return head
    f=s=head
    while(f.next!=None and f.next.next!=None):
        f=f.next.next
        s=s.next
    return s
def revr(head):
    if(head==None or head.next==None):
        return head
    n=revr(head.next)
    head.next.next=head
    head.next=None
    return n
def fstlst(head):
    m=findmid(head)
    sh=m.next
    m.next=None
    rsh=revr(sh)
    p=node(None)
    dummy=p
    while(head!=None and rsh!=None):
        dummy.next = head
        dummy = dummy.next
        head = head.next
        dummy.next = rsh
        dummy = dummy.next
        rsh = rsh.next
    if(head!=None):
        dummy.next=head
    if(rsh!=None):
        dummy.next=rsh
    return p.next
def traversal(head):
    if(head==None):
        print("ll is empty")
    else:
        while(head!=None):
            print(head.data,end=" ")
            head=head.next
        print()
l=[6,5,4,3,2,1]
n=len(l)
head=node(l[0])
temp=head
for i in range(1,n):
    temp.next=node(l[i])
    temp=temp.next
traversal(head)
head=fstlst(head)
traversal(head)



