#literally fibonacci
def stairs(n, dct):
    if n in dct:
        return dct[n]
    summ = 0
    if n == 0:
        return 1
    if n - 1 >= 0:
        summ += stairs(n-1, dct)
    if n - 2 >= 0:
        summ += stairs(n-2, dct)
    dct[n] = summ
    return summ

print(stairs(4, {}))