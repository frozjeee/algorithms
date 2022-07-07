def water(arr):
    i = 0
    j = len(arr) - 1
    max = 0
    while i != j:
        val = (j - i) * min(arr[j], arr[i])
        print(i, j)
        if max < val:
            max = val
        if arr[i] >= arr[j]:
            j -= 1
        else:
            i += 1

    return max

print(water([1,8,6,2,5,4,8,3,7]))
       