def maxProfit(prices) -> int:
    profit = 0
    n = len(prices)
    l = 0
    r = 1
    if n == 1:
        return 0
    while r < n:
        print(l, r)
        if prices[r] - prices[l] < 0:
            l = r
            r += 1
        else:
            print(prices[r] - prices[l])
            profit = max(profit, prices[r] - prices[l])
            r += 1
    return profit


print(maxProfit([7,6,4,3,1]))