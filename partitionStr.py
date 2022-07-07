# def solve(s):
#     arr = []
#     wordBorders = {}
#     word = [0, 0]
#     if not len(s):
#         return []
#     for i, l1 in enumerate(s):
#         if l1 in wordBorders:
#             wordBorders[l1] = [wordBorders[l1][0], i]
#         else:
#             wordBorders[l1] = [i, i]
            
#     for v in wordBorders.values():
#         if word[1] < v[0]:
#             arr.append(len(s[word[0]: word[1] + 1])
#             word = [v[0], v[1]]
#         elif word[1] < v[1]:
#             word[1] = v[1]
#     arr.append(s[word[0]: word[1] + 1])
#     for i in range(len(arr)):
#         arr[i] = len(arr[i])
#     return arr


def solve(s):
    last = {c: i for i, c in enumerate(s)}
    lo = r = 0
    res = []

    for hi, c in enumerate(s):
        r = max(r, last[c])
        if hi == r:
            res.append(hi - lo + 1)
            lo = r = hi + 1
    return res

print(solve("cocoplaydae"))

