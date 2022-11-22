class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, canBuy, t):
            if i >= len(prices):
                return 0
            if t == k:
                return 0
            if canBuy:
                return max(-prices[i] + dp(i + 1, False, t), dp(i + 1, True, t))
            else:
                return max(prices[i] + dp(i + 1, True, t + 1), dp(i + 1, False, t))
        
        return dp(0, True, 0)