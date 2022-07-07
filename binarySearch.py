def bSearch(arr, low, high, k):
    print(low, high)
    if low > high:
        return low - 1
    mid = int(low + (high - low) / 2)
    if arr:
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return bSearch(arr, low, mid, k)
        elif arr[mid] < k:
            return bSearch(arr, mid+1, high, k)
    else:
        return -1

print(bSearch([1,2,3,4,5,6], 0, 5, 7))