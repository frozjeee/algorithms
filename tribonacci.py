def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a = [0, 1, 1]
    for i in range(3, n + 1):
        a.append(a[i-1] + a[i-2], a[i-3])

    return a[n]