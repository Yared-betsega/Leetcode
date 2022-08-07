class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True
#         dp = [False] * len(nums)
#         for i in range(len(nums) - 2, -1, -1):
#             if nums[i] == 0:
#                 dp[i]  = False
#             elif i + nums[i] >= len(nums) - 1:
#                 dp[i] = True
#             else:
#                 if any(dp[i:i + nums[i] + 1]):
#                     dp[i] = True
                
#         return dp[0]
        @cache
        def chooseIndex(i):
            if i + nums[i] >= len(nums) - 1:
                return True
            for j in range(i + 1, i + nums[i] + 1):
                if chooseIndex(j):
                    return True
            return False
        return chooseIndex(0)

