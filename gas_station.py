def canCompleteCircuit(gas, cost) -> int:
    n = len(gas)
    total = curr = start = 0
    for i in range(n):
        total += gas[i] - cost[i]
        curr += gas[i] - cost[i]
        if curr < 0:
            curr = 0
            start = i + 1
    return -1 if total < 0 else start
    

print(canCompleteCircuit([1,2,3,4,3,2,4,1,5,3,2,4], [1,1,1,3,2,4,3,6,7,4,3,1]))