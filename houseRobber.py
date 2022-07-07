def rob(arr):
    for i in range(2, len(arr)):
        print(arr)
        arr[i] += max(arr[: i-1])
    return max(arr)

print(rob([1,2,3,1]))