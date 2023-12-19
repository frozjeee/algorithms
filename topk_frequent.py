from collections import defaultdict


def topKFrequent(nums, k):
    a = defaultdict(int)
    for i in nums:
        a[i] += 1
    a = [h for h, v in sorted(a.items(), key=lambda item: item[1], reverse=True)]
    return a[:k]
    

print(topKFrequent([1,1,1,2,2,3], 2))