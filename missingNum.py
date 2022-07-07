def missing(nums):
    summ = 0
    expected = 0
    for i in range(1, len(nums) + 1):
        expected += i
        summ += nums[i - 1]
    return expected - summ


print(missing([0, 1]))