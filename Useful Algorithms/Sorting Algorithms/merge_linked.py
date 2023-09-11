#linked
class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def merge(L1,L2):
    merged=Node("#")
    copy=merged
    while L1 and L2:
        if L1.val<L2.val:
            merged.next=L1
            merged=merged.next
            L1=L1.next
        else:
            merged.next=L2
            merged=merged.next
            L2=L2.next
    while L1:
        merged.next=L1
        merged=merged.next
        L1=L1.next
    while L2:
        merged.next=L2
        merged=merged.next
        L2=L2.next
    return copy.next

def get_mid(L):
    slow,fast=L,L.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

def mergesort(L):
    if not L or not L.next:
        return L
    left=L
    right=get_mid(L)
    tmp=right.next
    right.next=None
    right=tmp
    left=mergesort(left)
    right=mergesort(right)
    return merge(left,right)

def make_list(n):
    L=Node(0)
    copy=L
    for i in range(1,n):
        copy.next=Node(i%10)
        copy=copy.next
    return L

def print_list(L):
    while L:
        print(L.val,end=" ")
        L=L.next



a = Node(15)
b = Node(6)
c = Node(19)
d = Node(1)
e = Node(3)
f = Node(10)
g = Node(0)
h = Node(15)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

print_list(mergesort(a))