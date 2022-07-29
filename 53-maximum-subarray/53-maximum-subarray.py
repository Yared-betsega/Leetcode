class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i - 1], dp[i])
        return max(dp)

# time and space complexity
# time: O(n)
# space: O(n)