class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Bottom up approach
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]
        return dp[target]
    
        # Top down approach
        memo = {}
        def helper(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if target in memo:
                return memo[target]
            ans = 0
            for num in nums:
                ans += helper(target - num)
            memo[target] = ans
            return memo[target]
        
        return helper(target)
    
# time and space complexity
# time: O(nm)
# space: O(n)