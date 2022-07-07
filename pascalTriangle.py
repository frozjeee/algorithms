# def pascal(n):
#     a = [[1]]
#     for i in range(1, n):
#         k = []
#         for j in range(i + 1):
#             if j == 0 or j == i:
#                 k.append(1)
#             else:     
#                 k.append(a[i-1][j-1] + a[i-1][j])
#         a.append(k)
#     return a

# 1 100 101 1000 1 101 100 1 -

# def generate(numRows):
#     pascal = [[1]*(i+1) for i in range(numRows)]
#     for i in range(numRows):
#         for j in range(1,i):
#             pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
#     return pascal
######################################################################





def pascal(n):
    prev = [1]
    new = []
    for i in range(1, n + 1):
        new = [0 for i in range(i+1)]
        for j in range(len(prev) + 1):
            if j == 0 or j == len(prev):
                new[j] = 1
            else:     
                new[j] = (prev[j-1] + prev[j])
        prev = new
        new = []
    return prev


# class Solution(object):
#     def getRow(self, rowIndex):
#         """
#         :type rowIndex: int
#         :rtype: List[int]
#         """
#         row = [1]
#         for _ in range(rowIndex):
#             row = [x + y for x, y in zip([0]+row, row+[0])]
#         return row


print(pascal(4))