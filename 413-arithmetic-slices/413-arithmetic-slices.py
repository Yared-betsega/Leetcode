class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [0] * len(nums)
        for j in range(2, len(nums)):
            if nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                dp[j] = dp[j-1] + 1
                
        return sum(dp)

# time and space complexity
# time: O(n)
# space: O(n)