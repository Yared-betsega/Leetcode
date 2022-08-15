class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[cur_min]:
                cur_min = i
            else:
                max_profit = max(max_profit, prices[i] - prices[cur_min])
        return max_profit