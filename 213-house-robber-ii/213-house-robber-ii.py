class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
             return nums[0]
    
        dp = nums[:-1]
        for i in range(len(dp)):
            for j in range(i-1):
                dp[i] = max( nums[i] + dp[j], dp[i] )
            
        first = max(dp)
        
        dp = nums[1:]
        for i in range(len(dp)):
            for j in range(i-1):
                dp[i] = max( nums[i+1] + dp[j], dp[i] )
            
        second = max(dp)
        return max(first, second)
            