import random
from re import X
## O(n*log(n)) average 
# def quicksort(lst):
#     if len(lst) <= 1:
#         return lst
#     n = lst[random.randint(0, len(lst) - 1)]
#     lst.remove(n)
#     a = []
#     b = []
#     for i in range(len(lst)):
#         if n > lst[i]:
#             a.append(lst[i])
#         else:
#             b.append(lst[i])
#     return quicksort(a) + [n] + quicksort(b)

# g = []
# for _ in range(8):
#     g.append(random.randint(-100, 100))

# print(quicksort(g))


##################
## O(n*log(n)) average O(n^2) if there are equal element
# def Partition(arr, l, r):
#     global s
#     x = arr[l]
#     j = l
#     for i in range(l + 1, r):
#         print(s)
#         s += 1
#         if arr[i] <= x:
#             j += 1
#             arr[j], arr[i] = arr[i], arr[j]
#     arr[j], arr[l] = arr[l], arr[j]
#     return j


# def quicksort(arr, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r - 1)
#     arr[k], arr[l] = arr[l], arr[k]
#     m = Partition(arr, l, r)
#     quicksort(arr, l, m)
#     quicksort(arr, m + 1, r)
#     return arr
#############################################################
## O(n*log(n)) with equal elements too
def Partition(arr, l, r):
    global s
    x = arr[l]
    j1 = l
    j2 = j1
    for i in range(l + 1, r):
        print(s)
        s += 1
        if arr[i] < x:
            j1 += 1
            j2 += 1
            arr[j1], arr[i] = arr[i], arr[j1]
            if j1 != j2:
                arr[i], arr[j2] = arr[j2], arr[i]
        elif arr[i] == x:
            j2 += 1
            arr[i], arr[j2] = arr[j2], arr[i]
    arr[l], arr[j1] = arr[j1], arr[l]
    return [j1, j2]


def quicksort(arr, l, r):
    if l >= r:
        return
    k = random.randint(l, r - 1)
    arr[k], arr[l] = arr[l], arr[k]
    m1, m2 = Partition(arr, l, r)
    quicksort(arr, l, m1)
    quicksort(arr, m2 + 1, r)
    return arr



s = 0
print(quicksort([8,6,6,6,6,6,1], 0, 7))
# print(quicksort([16,83,73,27,98,34,94], 0, 7))