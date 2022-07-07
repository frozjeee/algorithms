def containsDuplicate(nums):
    return False if len(set(nums)) == len(nums) else True

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))