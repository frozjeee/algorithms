# def greedyKnapsack(arr, cap):
#     knapsack = [0 for _ in range(cap)]
#     V = 0
#     for j in range(len(arr)):
#         best = 0
#         if cap == 0:
#             return (V, knapsack)
#         for i, (v, w) in enumerate(arr):
#             if w > 0 and best < round(v / w, 2):
#                 best = i
#         a = min(cap, arr[best][1])
#         V += a * round(arr[best][0] / arr[best][1], 2)
#         arr[best][1] -= a
#         knapsack[j] += a
#         cap -= a
#     return (V, knapsack)


def repeatKnapsack(arr, cap):
    knapsack = [0 for _ in range(cap)]
    for we in range(1, cap):
        knapsack[we] = 0
        for v, w in arr:
            if w <= we:
                val = knapsack[we - w] + v
                if val > knapsack[we]:
                    knapsack[we] = val
    return knapsack

# not done and not understood
# def noRepeatKnapsack(arr, cap):
#     knapsack = [[0 for _ in range(cap)] for _ in range(len(arr))]
#     for i in range(len(arr)):
#         for w in range(1, cap):
#             knapsack[i][w] = knapsack[i][w - 1]
#             print(arr[i][1], w)
#             if arr[i][1] <= w:
#                 val = knapsack[i - 1][w - arr[i][1]] + arr[i][0]
#                 if knapsack[i][w] < val:
#                     knapsack[i][w] = val
#     return knapsack

print(repeatKnapsack([[20, 4], [14, 2], [18, 3]], 1231321))
# print(noRepeatKnapsack([[30, 6], [14, 3], [16, 4], [9, 2]], 11))   

