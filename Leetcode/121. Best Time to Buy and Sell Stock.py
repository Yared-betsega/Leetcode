#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        will_buy = prices[0]
        dp = 0
        for price in prices:
            if price < will_buy:
                will_buy = price
            else:
                dp = max(dp, price - will_buy)
        
        return dp

# time and space complexity
# time complexity = O(n)
# space complexity = O(1)
        
        
