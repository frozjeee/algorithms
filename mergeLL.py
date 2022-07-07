class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

c = ListNode(4)
b = ListNode(2, c)
a = ListNode(1, b)


d = ListNode(4)
f = ListNode(3, d)
e = ListNode(1, f)
# a.next = b
# a.next = ListNode(3)

def show(LL):
    cur = LL
    while cur:
        print(cur.val)
        cur = cur.next

def merge(head1, head2):
    dum = new = ListNode(0)
    while head1 and head2:
        if head1.val < head2.val:
            # print(new.next.val)
            new.next = head1
            head1 = head1.next
        else:
            new.next = head2
            head2 = head2.next
        new = new.next

    new.next = head1 or head2
    return dum.next

g = merge(a, e)
show(g)