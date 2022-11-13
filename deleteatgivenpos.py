class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def delatgivenpos(self,head,pos):
        if(head==None or pos<0):
            return head
        if(pos==0):
            head=head.next
        temp=head
        ptr=temp.next
        for i in range(pos-1):
            temp=temp.next
            ptr=ptr.next
        temp.next=ptr.next
        return head
    def traversal(self,head):
        if(head==None):
            print("ll is empty")
        temp=head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
        print()
l=[1,2,3,4,5]
n=len(l)
head=node(l[0])
temp=head
for i in range(1,n):
    temp.next=node(l[i])
    temp=temp.next
z=ll()
z.delatgivenpos(head,2)
z.traversal(head)

