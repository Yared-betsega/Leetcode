class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i, total):
            if i >= len(nums):
                return total
            cur = max(dp(i + 1, total), dp(i + 2, total + nums[i]))
            return cur
        return dp(0, 0)
    
#         dp = nums[:]
        
#         for i in range(len(nums)):
#             for j in range(i-1):
#                 dp[i] = max( nums[i] + dp[j], dp[i] )
            
#         return max(dp)

# time and space complexity
# time complexity = O(n ** 2)
# space complexity = O(n)
                
                