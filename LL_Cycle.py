def Cycle(head):
    while head:
        if isinstance(head.val, str):
            return True
        head.val = "visited"
        head = head.next
    return False


# Tortoise and hare algorithm
# def hasCycle(head):
#     if not head:
#         return False 
#     slow, fast = head, head
#     while True:
#         slow = slow.next
#         fast = fast.next
#         if fast != None:
#             fast = fast.next
#         if slow == None or fast == None:
#             return False
#         if slow == fast:
#             return True