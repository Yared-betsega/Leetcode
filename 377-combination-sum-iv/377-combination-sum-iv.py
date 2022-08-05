class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
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