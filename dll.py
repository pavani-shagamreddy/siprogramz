class node:
    def __init__(self,data=None):
        self.data=data
        self.prev = None
        self.next=None

class ll:
    def insertatbegin(self,head,tail,key):
        if(head==None):
            newnode=node(key)
            head=newnode
            tail=newnode
            return head
        newnode=node(key)
        newnode.next=head
        head.prev=newnode
        head=newnode
        return head
    def insertatend(self,head,tail,key):
        if(head==None):
            newnode = node(key)
            head = newnode
            tail = newnode
            return head
        newnode=node(key)
        tail.next=newnode
        newnode.prev=tail
        tail=newnode
        return head
    def insertatgivenpos(self,head,pos,key):
        temp=head
        ptr=temp.next
        newnode=node(key)
        for i in range(pos-2):
            temp=temp.next
            ptr=ptr.next
        newnode.next=temp.next  #or newnode.next=ptr
        newnode.prev=temp
        temp.next=newnode
        ptr.prev=newnode
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
            head.prev=None  #imp point to remember
            return head
    def delatend(self,head,tail):
        if(head==None or head==tail):
            head=tail=None
            print("ll is empty")
        else:
            """
            temp=head
            while(temp.next.next!=tail):
                temp=temp.next
            temp.next=None
            tail=temp
            return head
            no need of doing above method"""
            temp=tail.prev
            temp.next=None
            tail=temp
            return head
    def delatgivenpos(self,head,pos):
        temp=head
        ptr=temp.next
        for i in range(pos-2):
            temp=temp.next
            ptr=ptr.next
        temp.next=ptr.next
        t=ptr.next
        t.prev=temp
        return head

l=[4,5,6,7,8,9,10]
n=len(l)
head=node(l[0])
tail=node(l[0])
temp=head
for i in range(1,n):
    nn=node(l[i])
    temp.next=nn
    nn.prev=temp
    tail=nn
    temp=temp.next
z=ll()
z.traversal(head,tail)
