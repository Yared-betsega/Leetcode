class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def bottom_up(nums):
            dp = nums[:]
            neg = -1 if dp[0] >= 0 else 0
            for i in range(1, len(nums)):
                if nums[i] == 0:
                    if neg != -1 and i - 1 != neg:
                        dp[i - 1] = dp[i - 1] // dp[neg]
                    dp[i] = 0
                    neg = -1
                elif nums[i] < 0:
                    dp[i] = dp[i - 1] * nums[i] if dp[i - 1] != 0 else nums[i]
                    neg = i if neg == -1 else -1
                else:
                    dp[i] = dp[i - 1] * nums[i] if dp[i - 1] != 0 else nums[i]
            return max(dp)
        
        return max(bottom_up(nums), bottom_up(nums[::-1]))