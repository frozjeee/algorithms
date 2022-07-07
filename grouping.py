def grouping(arr):
    R = []
    i = 0
    l = 0
    while i < len(arr) - 1:
        val = arr[i]
        l = i
        while i < len(arr) - 1 and arr[i + 1] - val <= 1:
            print(i)
            i += 1
        i += 1
        R.append([arr[j] for j in range(l, i)])

    R = []
    i = 0
    j = 0
    while i <= len(arr) - 1:
        a = []
        [l, r] = [arr[i], arr[i] + 1]
        i += 1
        while i <= len(arr) - 1 and arr[i] <= r:
            print(arr[i])
            a.append(arr[i])

            i += 1
        R.append(a)
    return R 

print(grouping([1,10,11,12,13,13,13,20,22,23]))
