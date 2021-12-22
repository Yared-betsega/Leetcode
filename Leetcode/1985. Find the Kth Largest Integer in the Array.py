def kthLargestNumber(nums, k):
    nums = list(map(int, nums))
    nums = sorted(nums, reverse=True)
    return nums[k-1]


print(kthLargestNumber(["2", "21", "12", "1"], 3))
