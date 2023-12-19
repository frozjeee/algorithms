from collections import Counter, defaultdict


def isNStraightHand(hand, groupSize):
    n = len(hand)
    cntr = Counter(hand)
    hand.sort()
    if n % groupSize != 0:
        return False
    g = list({value: True for value in hand})
    i = 0
    while i + groupSize <= len(g):
        print(i)
        v = g[i]
        rn = range(v, v + groupSize)
        specific_values = {key: value for key, value in cntr.items() if key in rn and value > 0}
        if len(specific_values) < groupSize:
            i += 1
            continue
        min_num = min(specific_values)
        min_dict = {key: specific_values[min_num] for key in specific_values.keys()}
        print(min_dict)
        cntr.subtract(min_dict)
        i += g.index(min_num)
    print(cntr)
    return True if max(cntr.values()) == 0 else False

print(isNStraightHand([1,2,3,4,5,6], 2))


# 1 2 2 3 3 4 7 8 9

# 1 2 3 4 7 8 9

# 6 6 7 7 7 7 8 8 9 10
# 6 7 / 6 7/ 7 8/ 7 8/ 9 10