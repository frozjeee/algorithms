def maxSub(nums):
    for i in range(1, len(nums)):
        print(nums)
        nums[i] = max(nums[i], nums[i] + nums[i - 1])
    return max(nums)

print(maxSub([-2,1,-3,4,-1,2,1,-5,4]))

