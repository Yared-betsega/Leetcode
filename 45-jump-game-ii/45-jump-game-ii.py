class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # Single loop O(n) Solution
        if len(nums) == 1:
            return 0
        maxReach, steps = nums[0], 1
        i = 0
        while i < len(nums):
            if maxReach >= len(nums) - 1:
                return steps
            temp = 0
            while i < len(nums) and i <= maxReach:
                temp = max(temp, i + nums[i])
                i += 1
            maxReach = temp
            steps += 1
        return steps
                
                
            
        
        # Dynamic Programming Top Down Approach
        @cache
        def chooseIndex(i):
            if i >= len(nums) - 1:
                return 0
            ans = float("inf")
            for j in range(i + 1, i + nums[i] + 1):
                ans = min(ans, chooseIndex(j) + 1)
            return ans
        return chooseIndex(0)
        
        # Dynamic Programming Bottom Up Approach
        if len(nums) == 1:
            return 0
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)):
                dp[j] = min(dp[j], dp[i] + 1)
            
                
        return dp[-1]

            