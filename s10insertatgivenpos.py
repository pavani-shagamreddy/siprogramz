class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class ll:
    def insertatgivenpos(self,head,pos,key):
        temp=head
        newnode=node(key)
        for i in range(pos-1):
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
l=[4,5,6,7,8,9,10]
n=len(l)
for i in range(n):
    nn=node(l[i])
    head.next=nn
    head=head.next
z=ll()
z.traversal(temp.next)
head=z.insertatgivenpos(temp.next,2,10)
z.traversal(head)
