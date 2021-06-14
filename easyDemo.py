def demo(nums):
    i = 0
    sb = 0
    ls = 0
    while i < len(nums) - 2:
        if nums[i] > nums[i+1]:
            sb += 1
            print(ls, nums[i+1], nums[i])
            if sb > 1 or (ls < nums[i+1] and ls > nums[i]):
                return False
        ls = nums[i]
        i += 1
    print("TRue")
    return True


demo([3, 4, 2, 3])
