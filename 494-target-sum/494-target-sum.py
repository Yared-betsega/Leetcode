class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, target):
            if i > len(nums):
                return 0
            if i == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0
            
            return dp(i + 1, target + nums[i]) + dp(i + 1, target - nums[i])
        
        return dp(0, target)