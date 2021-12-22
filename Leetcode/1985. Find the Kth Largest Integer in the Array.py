def kthLargestNumber(nums, k):
    nums = list(map(int, nums))
    nums = sorted(nums, reverse=True)
    return str(nums[k-1])
