# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = nums[:]
        
        for i in range(len(nums)):
            for j in range(i-1):
                dp[i] = max( nums[i] + dp[j], dp[i] )
            
        return max(dp)

# time and space complexity
# time complexity = O(n ** 2)
# space complexity = O(n)
                
                
