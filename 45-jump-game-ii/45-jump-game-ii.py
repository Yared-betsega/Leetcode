class Solution:
    def jump(self, nums: List[int]) -> int:
        # maxReach, steps = nums[0], {}
        # for i in range(len(nums)):
        #     if 
        
        
        # @cache
        # def chooseIndex(i):
        #     if i >= len(nums) - 1:
        #         return 0
        #     ans = float("inf")
        #     for j in range(i + 1, i + nums[i] + 1):
        #         ans = min(ans, chooseIndex(j) + 1)
        #     return ans
        # return chooseIndex(0)
        
        if len(nums) == 1:
            return 0
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                dp[j] = min(dp[j], dp[i] + 1)
            
                
        return dp[-1]

            