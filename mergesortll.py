#mergesort of linkedlist
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def findmid(head):
    if(head==None):
        return head
    fast=s=head
    while(fast.next!=None and fast.next.next!=None):
        fast=fast.next.next
        s=s.next
    return s
def merge(head1,head2):
    p=node(None)
    dummy=p
    while(head1!=None and head2!=None):
        if(head1.data<head2.data):
            dummy.next=head1
            head1=head1.next
            dummy=dummy.next
        else:
            dummy.next = head2
            head2 = head2.next
            dummy = dummy.next
    if(head1!=None):
        dummy.next=head1
    if(head2!=None):
        dummy.next=head2
    return p.next
def ms(head):
    if(head.next==None):
        return head
    m=findmid(head)
    sh=m.next
    m.next=None
    return merge(ms(head),ms(sh))
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
head=ms(head)
traversal(head)



