class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class ll:
    def insertatbegin(self,head,tail,key):
        if(head==None):
            newnode=node(key)
            head=newnode
            tail=newnode
            tail.next=head
            return head
        newnode=node(key)
        newnode.next=head
        head=newnode
        tail.next=head
        return head
    def insertatend(self,head,tail,key):
        if(head==None):
            newnode = node(key)
            head = newnode
            tail = newnode
            tail.next=head
            return head
        newnode=node(key)
        tail.next=newnode
        tail=newnode
        tail.next=head
        return head
    def insertatgivenpos(self,head,tail,pos,key):
        temp=head
        newnode=node(key)
        for i in range(pos-2):
            temp=temp.next
        newnode.next=temp.next
        temp.next=newnode
        return head
    def traversal(self,head,tail):
        if(head==None):
            print("LL is empty")
        else:
            temp=head
            while(temp!=tail):
                print(temp.data,end=" ")
                temp=temp.next
            print(temp.data)
    def delatbegin(self,head,tail):
        if(head==None or head==tail):
            head=None
            tail=None
            print("LL is empty")
        else:
            head=head.next
            tail.next=head
            return head
    def delatend(self,head):
        if(head==None or head==tail):
            head=tail=None
            print("ll is empty")
        else:
            temp=head
            while(temp.next.next!=tail):
                temp=temp.next
            temp.next=head
            tail=temp
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
tail=node()
temp=head
l=[4,5,6,7,8,9,10]
n=len(l)
for i in range(n):
    nn=node(l[i])
    tail=nn
    head.next=nn
    head=head.next
tail.next=temp.next
z=ll()
z.traversal(temp.next,tail)
