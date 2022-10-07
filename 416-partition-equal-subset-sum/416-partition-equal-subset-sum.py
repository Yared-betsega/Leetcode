class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot & 1:
            return False
        tot //= 2
        
        # Top down approach
#         @cache
#         def dp(i, l):
#             if l == tot:
#                 return True
#             if l > tot:
#                 return False
#             if i >= len(nums):
#                 return False
#             return dp(i + 1, l + nums[i]) or dp(i + 1, l)
        
#         return dp(0, 0)


        dp = [False] * (tot + 1)
        dp[0] = True
        for num in nums:
            for i in range(tot, -1, -1):
                if dp[i]:
                    if i + num < len(dp):
                        dp[i + num] = True
        return dp[tot]