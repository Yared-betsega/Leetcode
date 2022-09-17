class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, canBuy, t):
            if i >= len(prices):
                return 0
            if t == 2:
                return 0
            
            if canBuy:
                return max(-prices[i] + dp(i + 1, False, t), dp(i + 1, True, t))
            else:
                return max(prices[i] + dp(i + 1, True, t + 1), dp(i + 1, False, t))
        
        return dp(0, True, 0)