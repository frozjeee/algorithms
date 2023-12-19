def jump(nums):
    lst = [0] * len(nums)
    i = 1
    k = 0
    while lst[-1] == 0:
        if nums[k] - i + k >= 0:
            lst[i] = 1 + lst[k]
            i += 1
        else:
            k += 1
    return lst


print(jump([2,3,1,1,4]))




# def jump(nums):
#     ans = 0
#     end = 0
#     farthest = 0

#     # Implicit BFS
#     for i in range(len(nums) - 1):
#         farthest = max(farthest, i + nums[i])
#         if farthest >= len(nums) - 1:
#             ans += 1
#             break
#         if i == end:      # Visited all the items on the current level
#             ans += 1        # Increment the level
#             end = farthest  # Make the queue size for the next level

#     return ans