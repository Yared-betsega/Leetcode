class Solution:
    def numDecodings(self, s: str) -> int:
        # Bottom up solution
        dp = [0] * (len(s) + 1)
        dp[len(s) - 1] = 1 if s[-1] != "0" else 0
        dp[-1] = 1
        for i in range(len(s) - 2, -1, -1):
            if int(s[i]) != 0:
                dp[i] += dp[i + 1]
                if int(s[i: i + 2]) <= 26:
                    dp[i] += dp[i + 2]
        
        return dp[0]
            
        '''
        memo = {}
        def dp(idx):
            if idx == len(s) - 1:
                return 1
            if idx in memo:
                return memo[idx]
            ans = 0
            if s[idx + 1] != "0":
                ans += dp(idx + 1)
                if idx + 2 < len(s) and int(s[idx +1: idx + 3]) <= 26:
                    ans += dp(idx + 2)
            memo[idx] = ans
            return memo[idx]
        
        return dp(-1)
    
# time and space complexity
# time: O(n)
# space: O(n)

        '''