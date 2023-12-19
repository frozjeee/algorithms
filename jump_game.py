def canJump(nums) -> bool:
    i = 0
    left = nums[0]
    if len(nums) == 1:
        return True
    while i < len(nums) - 1:
        print(i, left)
        if left <= nums[i + 1] and left:
            i += 1
            left = nums[i]
        elif left > nums[i + 1] and left:
            i += 1
            left -= 1
        elif not left:
            left = nums[i]
        if not left and nums[i] == 0 and i < len(nums) - 1:
            print(left)
            return False

    return True if i >= len(nums) - 1 else False



print(canJump([3,0,0,0]))

