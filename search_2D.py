def searchMatrix(matrix, target: int) -> bool:
    m = len(matrix[0]) - 1
    n = 0
    while m >= 0 and n <= len(matrix) - 1:
        print(n, m)
        start = matrix[n][m]
        print(start)
        if start > target:
            m -= 1
        elif start < target:
            n += 1
        else:
            return True
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))