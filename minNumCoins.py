# a lot of time
# def recursiveChange(money, coins):
#     if money == 0:
#         return 0
#     minNumCoins = float("inf")
#     for coin in [1, *coins]:
#         if money >= coin:
#             numCoins = recursiveChange(money - coin, coins)
#             if numCoins + 1 < minNumCoins:
#                 minNumCoins = numCoins + 1
#     return minNumCoins


def DPChange(money, coins):
    if money == 0:
        return 0
    


print(DPChange(12, [6,5]))


        

