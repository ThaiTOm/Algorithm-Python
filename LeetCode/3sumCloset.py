def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    sm = 99999
    i = 0
    nums.sort()
    cl = 999999
    while i < len(nums):
        x = i+1
        y = len(nums) - 1
        while x < len(nums) and y > x:
            val = nums[x] + nums[y] + nums[i]
            if abs(target - val) < cl:
                sm = val
                cl = abs(target - val)
            elif val < target:
                x += 1
            else:
                y -= 1
        i += 1
    return sm
