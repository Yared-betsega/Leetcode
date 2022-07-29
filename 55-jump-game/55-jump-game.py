class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [False] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                dp[i]  = False
            elif i + nums[i] >= len(nums) - 1:
                dp[i] = True
            else:
                for j in range(i+1, i + nums[i] + 1):
                    if dp[j]:
                        dp[i] = True
        return dp[0]