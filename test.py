def findDuplicate(nums) -> int:
    i=0
    while i <len(nums):
        print(nums)
        if i == nums[i] - 1:
            i=i+1
            continue
        if nums[nums[i] - 1] == nums[i]:
            return nums[i]
        else:
            t = nums[i]
            nums[i] = nums[t - 1]
            nums[t - 1] = t

