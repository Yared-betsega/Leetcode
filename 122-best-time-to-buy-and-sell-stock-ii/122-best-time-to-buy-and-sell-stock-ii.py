class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         will_buy = prices[0]
#         ans = []
#         dp = 0
#         for i in range(1, len(prices)):
#             if prices[i] < prices[i - 1]:
#                 heappush(ans, -dp)
#                 dp = 0
#                 will_buy = prices[i]
#             else:
#                 dp = max(dp, prices[i] - will_buy)
#         heappush(ans, -dp)
#         return -sum(ans)

# # time and space complexity
# # time: O(nlog(n))
# # space: O(n)

        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans

# time and space complexity
# time: O(n)
# space: O(1)