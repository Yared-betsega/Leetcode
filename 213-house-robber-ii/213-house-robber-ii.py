class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
             return nums[0]
        @cache
        def dp(i, inc, total):
            if i >= len(nums):
                return total
            if i == len(nums) - 1:
                if inc:
                    return total
            cur = max(dp(i + 1, False if i == 0 else inc, total), dp(i + 2, inc, total + nums[i]))
            return cur
        
        return dp(0, True, 0)
        
            