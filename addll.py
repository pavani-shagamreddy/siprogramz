class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def rev(head):
    if(head==None or head.next==None):
        return head
    n=rev(head.next)
    head.next.next=head
    head.next=None
    return n
def add(h1,h2):
    carry=0
    p=node(None)
    dummy=p
    while(h1!=None and h2!=None):
        dummy.next=node((h1.data+h2.data+carry)%10)
        dummy=dummy.next
        carry=(h1.data+h2.data+carry)//10
        h1=h1.next
        h2=h2.next

    while(h1!=None):
        dummy.next=node((h1.data+carry)%10)
        dummy = dummy.next
        carry = (h1.data + carry) // 10
        h1 = h1.next
    while (h2 != None):
        dummy.next = node((h2.data + carry) % 10)
        dummy = dummy.next
        carry = (h2.data + carry) // 10
        h2 = h2.next
    return p.next

def summ(h1,h2):
    return rev(add(rev(h1),rev(h2)))
def traversal(head):
    if(head==None):
        print("ll is empty")
    else:
        while(head!=None):
            print(head.data,end=" ")
            head=head.next
        print()
l1=[7,8,1]
l2=[5,6]
h1=node(l1[0])
h2=node(l2[0])
t1=h1
t2=h2
for i in range(1,len(l1)):
    t1.next=node(l1[i])
    t1=t1.next
for i in range(1,len(l2)):
    t2.next=node(l2[i])
    t2=t2.next
z=summ(h1,h2)
traversal(z)
