class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        dur = [1, 7, 30]
        @cache
        def dp(day):
            if day > 365:
                return 0
            if day not in days:
                return dp(day + 1)
            ans = float("inf")
            for i in range(3):
                ans = min(ans, costs[i] + dp(day + dur[i]))
            return ans
        
        return dp(1)
#         days = set(days)
#         dur = [1, 7, 30]
#         dp = [0] * 365
#         i = 0
#         while i <= 365:
#             if i in days:
#                 start = dp[i]
#                 for j in range(3):
#                     for k in range(i, min(365, i + dur[j])):
#                         if dp[k] == float("inf"):
#                             dp[k] = costs[j]
#                         dp[k] = min(dp[k], start + costs[j])
#                 i = k + 1
#             else:
#                 i += 1

                