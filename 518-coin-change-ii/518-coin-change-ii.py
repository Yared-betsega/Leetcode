class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        
        # Bottom up
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(amount):
                if i + j <= amount:
                    dp[i + j] += dp[j]
            
        return dp[amount]
        
        
        
        
        
        dp = {}
        def helper(index, amount):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if amount in dp:
                return dp[amount]
            
            dp[amount] = 0
            for i in range(len(coins)):
                dp[amount] += helper(i, amount - coins[i]) 
            return dp[amount]
        ans = helper(0, amount - coins[0])
        return ans 