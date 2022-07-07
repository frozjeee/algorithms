#Greatest divider of a and b
import math
def GCD(a, b):
    if b == 0:
        return a
    c = a % b
    print(f"a={a}  b={b}  c={c}")
    return GCD(b, c)

print(GCD(123132, 123124124))

