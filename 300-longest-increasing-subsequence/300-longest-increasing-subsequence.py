class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = [1] * len(nums)
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[j] + 1, dp[i])
        
#         return max(dp)

# # time and space complexity
# # time: O(n**2)
# # space: O(n)
        @cache
        def dfs(index):
            c = 0
            ans = 0
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index]:
                    ans = max(ans, dfs(i) + 1)
                    c += 1
            if c == 0:
                return 1
            else:
                return ans
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        return ans