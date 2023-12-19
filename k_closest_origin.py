import heapq
import math


def kClosest(points, k):
    heap = []
    b = []
    for i in points:
        heapq.heappush(heap, (round(math.sqrt(i[0]**2 + i[1]**2), 5), [i[0],i[1]]))
    
    for _ in range(k):
        print(heap)
        b.append(heapq.heappop(heap)[1])

    return b

print(kClosest([[1,3],[-2,2],[2,-2]], 2))