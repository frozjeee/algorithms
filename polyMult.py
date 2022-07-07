## O(n^2), accurateTime(n^2 + n)
def polyMult(A, B, n):
    product =  []
    for _ in range((2*n - 2) + 1):
        product.append(0)
    for i in range(n):
        for j in range(n):
            product[i + j] = product[i + j] + A[i] * B[j]
    return product




print(polyMult([1, 2, -1], [2, -3, 6], 3))