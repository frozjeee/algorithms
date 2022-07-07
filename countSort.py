## O(n+count(or k)) or more 
### first try by definition 
# def countSort(arr):
#     max = 0
#     result = []
#     for i in arr:
#         if max < i:
#             max = i
#     count = [0 for _ in range(max)]
#     for i in range(len(arr)):
#         count[arr[i] - 1] += 1
#     for i in range(len(count)):
#         if count[i] > 0:
#             for _ in range(count[i]):
#                 result.append(i+1)
#     return result

## O(n+M) or O(n) if n == M 
def countSort(arr):
    max = 0
    result = [0 for _ in range(len(arr))]
    for i in arr:
        if max < i:
            max = i
    count = [0 for _ in range(max + 1)]
    pos = [0 for _ in range(max + 1)]
    for i in range(len(arr)):
        count[arr[i]] += 1
    print(count)
    for i in range(1, len(pos)):
        pos[i] = pos[i-1] + count[i]
    print(pos)
    for i in range(len(arr)):
        result[pos[arr[i]]] = arr[i]
        pos[arr[i]] -= 1
    return result

print(countSort([16,83,73,0,27,98,34,94,16]))

