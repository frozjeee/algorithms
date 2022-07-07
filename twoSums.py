def twoSum(arr, target):
    dct = {}
    for i in range(len(arr)):
        if target - arr[i] in dct:
            return [dct[target-arr[i]], i]
        dct[arr[i]] = i

print(twoSum([3,3], 6))