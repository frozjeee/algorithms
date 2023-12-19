from collections import defaultdict


def min_exc_none(a, b):
    if a is None:
        return b
    elif b is None:
        return a
    else:
        return min(a, b)

memo = {}
def bottom_up(n, coins):
    if n in memo:
        return memo[n]
    if n == 0:
        answer = 0
    else:
        answer = None
    for coin in coins:
        val = n - coin
        if val < 0:
            continue
        else:
            answer = min_exc_none(answer, bottom_up(val, coins) + 1)
    memo[n] = answer
    return answer


# print(bottom_up(7, [1,3,5]))


def memo_sol(n, coins):
    memo = {}
    memo[0] = 0
    for i in range(1, n + 1):
        for coin in coins:
            val = i - coin
            if val < 0:
                continue
            else:
                memo[i] = min_exc_none(memo.get(i), memo.get(val) + 1)
    print(memo)
    return memo[n]


# print(memo_sol(7, [1,3,5]))


def how_many_ways(n, coins):
    memo = defaultdict(lambda _: 0)
    memo[0] = 1

    for i in range(1, n + 1):
        memo[i] = 0

        for coin in coins:
            val = i - coin
            if val < 0:
                continue
            else:
                print(memo)
                memo[i] = memo[i] + memo[val]

    return memo[n]


# print(how_many_ways(7, [1,3,5]))

def maze(n, m):
    memo = {}
    for i in range(1, n + 1):
        memo[(i, 1)] = 1
    for j in range(1, m + 1):
        memo[(1, j)] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]
    return memo[(n, m)]


print(maze(18, 6))