class Solution:
    def numDecodings(self, s: str) -> int:
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