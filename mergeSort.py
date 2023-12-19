def Merge(B, C):
    D = []
    while B and C:
        b = B[0]
        c = C[0]
        if b <= c:
            D.append(b)
            B.pop(0)
        else:
            D.append(c)
            C.pop(0)
    D += C
    D += B
    return D
## roughly O(n*log(n))
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    m = int(len(arr) / 2)
    B = mergeSort(arr[:m])
    C = mergeSort(arr[m:])
    A = Merge(B, C)
    return A    

print(mergeSort([16,83,73,27,98,34,94]))