#program 2 insert an ele in to sorted linked list
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class ll:
    def sorted(self,head,key):
        temp=head
        newnode=node(key)
        while(temp.next!=None and temp.next.data<key):
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
        return head
    def traversal(self,head):
        if(head==None):
            print("LL is empty")
        else:
            temp=head
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
            print()
head=node()
temp=head
l=[4,5,6,8,9,10]
n=len(l)
for i in range(n):
    nn=node(l[i])
    head.next=nn
    head=head.next
z=ll()
z.traversal(temp.next)
head=z.sorted(temp.next,7)
z.traversal(head)
