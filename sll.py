class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
def insertatbegin(head,key):
    if(head==None):
        return node(key)
    newnode=node(key)
    newnode.next=head
    head=newnode
    return head
def insertatend(head,key):
    if(head==None):
        return node(key)
    temp=head
    newnode=node(key)
    while(temp.next!=None):
        temp=temp.next
    temp.next=newnode
    return head
def insertatgivenpos(head,pos,key):
    temp=head
    newnode=node(key)
    for i in range(pos-2):
        temp=temp.next
    newnode.next=temp.next
    temp.next=newnode
    return head
def traversal(head):
    if(head==None):
        print("LL is empty")
    else:
        temp=head
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
        print()
def delatbegin(head):
    if(head==None):
        print("LL is empty")
    else:
        head=head.next
        return head
def delatend(head):
    if(head==None or head.next==None):
        print("ll is empty")
    else:
        temp=head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
        return head
def delatgivenpos(head,pos):
    temp=head
    ptr=temp.next
    for i in range(pos-2):
        temp=temp.next
        ptr=ptr.next
    temp.next=ptr.next
    return head
head=node(3)
head.next=node(4)
head.next.next=node(5)
head.next.next.next=node(6)
traversal(head)
head=delatgivenpos(head,2)
traversal(head)