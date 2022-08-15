class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            j = i
            if nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                while j >= 2 and nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                    dp[i] += 1
                    j -= 1
        return sum(dp)