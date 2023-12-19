def findDuplicate(nums):
    slow = fast = finder = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        print(f"slow = {slow}, fast = {fast}")
        if slow == fast:
            while finder != slow:
                finder = nums[finder]
                slow = nums[slow]
                print(f"slow = {slow}, finder = {finder}")
            return finder
        

print(findDuplicate([10,3,4,2,2]))