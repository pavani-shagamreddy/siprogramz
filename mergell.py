#merge 2 sorted linkedlists
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
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
def traversal(head):
    if(head==None):
        print("ll is empty")
    else:
        while(head!=None):
            print(head.data,end=" ")
            head=head.next
        print()

l1=[1,3,5,6]
l2=[2,4]
n1=len(l1)
n2=len(l2)
head1=node(l1[0])
head2=node(l2[0])
temp1=head1
temp2=head2
for i in range(1,n1):
    temp1.next=node(l1[i])
    temp1=temp1.next
for i in range(1,n2):
    temp2.next=node(l2[i])
    temp2=temp2.next
traversal(head1)
traversal(head2)
p=merge(head1,head2)
traversal(p)




