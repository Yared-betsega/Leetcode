class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        @lru_cache(None)
        def dp(i, state = 0):
            if i == len(s):
                return 0
            if s[i] == "0":
                if state == 1:
                    return 1 + dp(i + 1, 1)
                
                return min(dp(i + 1, 0), 1 + dp(i + 1, 1))
            else:
                if state == 1:
                    return dp(i + 1, 1)
                return min(dp(i + 1, 1), 1 + dp(i + 1, 0))
            
        
        return dp(0)