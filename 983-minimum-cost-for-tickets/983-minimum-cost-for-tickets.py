class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         days = set(days)
#         dur = [1, 7, 30]
#         @cache
#         def dp(day):
#             if day > 365:
#                 return 0
#             if day not in days:
#                 return dp(day + 1)
#             ans = float("inf")
#             for i in range(3):
#                 ans = min(ans, costs[i] + dp(day + dur[i]))
#             return ans
#         return dp(1)
        n = days[-1]
        days = set(days)
        dp = [0] * (n + 1)
        for i in range(1, len(dp)):
            if i in days:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(i - 7, 0)] + costs[1], dp[max(i - 30, 0)] + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
            