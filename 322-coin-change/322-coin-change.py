class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def helper(amount):
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            
            dp[amount] = float("inf")
            for i in coins:
                dp[amount] = min(dp[amount], helper(amount - i) + 1)
            return dp[amount]
        ans = helper(amount)
        return ans if ans != float("inf") else -1