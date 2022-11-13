class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class ll:
    def insertatbegin(self,head,key):
        if(head==None):
            return node(key)
        newnode=node(key)
        newnode.next=head
        head=newnode
        return head
    def insertatend(self,head,key):
        if(head==None):
            return node(key)
        temp=head
        newnode=node(key)
        while(temp.next!=None):
            temp=temp.next
        temp.next=newnode
        return head
    def insertatgivenpos(self,head,pos,key):
        temp=head
        newnode=node(key)
        for i in range(pos-2):
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
    def delatbegin(self,head):
        if(head==None):
            print("LL is empty")
        else:
            head=head.next
            return head
    def delatend(self,head):
        if(head==None or head.next==None):
            print("ll is empty")
        else:
            temp=head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
            return head
    def delatgivenpos(self,head,pos):
        temp=head
        ptr=temp.next
        for i in range(pos-2):
            temp=temp.next
            ptr=ptr.next
        temp.next=ptr.next
        return head
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
