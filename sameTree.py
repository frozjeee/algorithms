import collections


# def same(p, q):
#     q1 = collections.deque([p])
#     q2 = collections.deque([q])
#     while q1 and q2:
#         q1len = len(q1)
#         q2len = len(q2)
#         if q1len != q2len:
#             return False

#         for _ in range(q1len):
#             node1 = q1.popleft()
#             node2 = q2.popleft()
#             if node1 and node2:
#                 if node1.val != node2.val:
#                     return False
#                 if node1.left or node2.left:
#                     q1.append(node1.left)
#                     q2.append(node2.left)
#                 if node1.right or node2.right:
#                     q1.append(node1.right)
#                     q2.append(node2.right)
#             elif (not node1) and (not node2):
#                 continue
#             else:
#                 return False
#     return True


def isSameTree3(p, q):
    queue = [(p, q)]
    while queue:
        node1, node2 = queue.pop(0)
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    return True
            
        