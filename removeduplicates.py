#remove all duplicates of ll....
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def remdup(self,head,n,x):
        if head==None:
            print("ll is empty")
        temp=head
        while(head.next!=None):
            if(head.next.data==x):
                head.next=head.next.next
            else:
                head=head.next
        if(temp.data==x):
            return temp.next
        return temp
    def traversal(self,head):
        if(head==None):
            print("ll is empty")
        temp=head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
        print()
l=[1,2,2,4,5]
n=len(l)
head=node(l[0])
temp=head
for i in range(1,n):
    temp.next=node(l[i])
    temp=temp.next
z=ll()
head=z.remdup(head,n,5)
z.traversal(head)
