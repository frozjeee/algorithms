from math import log2
#my solution O(n)
def bits(n):
    nums = [0]
    k = 0
    for i in range(1, n + 1):
        if int(log2(i)) ==  log2(i):
            k = 0
        nums.append(nums[k] + 1)
        k += 1
    return nums

# solution O(n)
# def countBits(num: int):
#     counter = [0]
#     for i in range(1, num+1):
#         print(counter[i >> 1])
#         counter.append(counter[i >> 1] + i % 2)
#     return counter


# print(countBits(6))

#                         8     11
# 0 # 1 # 1 2 # 1 2 2 3 # 1 2 2 3 2 3 3 4 # 1 2 2 3 2 3 3 4 2 3 3 4 3 4 4 5
