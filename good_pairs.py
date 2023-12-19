import math
from collections import defaultdict


def numIdenticalPairs(nums):
    a = defaultdict(int)
    b = 0
    for i in nums:
        b += a[i]
        a[i] += 1
    return b

print(numIdenticalPairs([1,2,3,1,1,3]))
