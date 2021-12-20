def targetIndices(nums, target):
    nums = sorted(nums)
    length = len(nums)
    ans = []
    for i in range(length):
        if nums[i] == target:
            ans.append(i)
    return ans