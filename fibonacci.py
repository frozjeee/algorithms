# from functools import cache


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = [0, 1]
    for i in range(2, n + 1):
        a.append(a[i-1] + a[i-2])

    return a[n]

a = fib(100)

print(a)



# @cache
# def fib(n):
#     if n in [1, 2]:
#         return 1

#     return fib(n-1) + fib(n-2)

# print(fib(100))