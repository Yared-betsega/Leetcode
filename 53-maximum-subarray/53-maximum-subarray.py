class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        maxSub = dp
        for i in range(1, len(nums)):
            dp = max(nums[i] + dp, nums[i])
            maxSub = max(maxSub, dp)
        return maxSub

# time and space complexity
# time: O(n)
# space: O(1)