class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, canBuy):
            if i >= len(prices):
                return 0
            
            if canBuy:
                return max(-prices[i] + dp(i + 1, False), dp(i + 1, True))
            else:
                return max(prices[i] + dp(i + 2, True), dp(i + 1, False))
        
        return dp(0, True)