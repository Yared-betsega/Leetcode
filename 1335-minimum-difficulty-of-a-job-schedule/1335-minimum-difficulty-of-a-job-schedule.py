class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
#         @cache
#         def dp(i, d, _mx):
#             if i >= len(jobDifficulty):
#                 if not d: return _mx
#                 else: return float("inf")     
#             if d < 0: return float("inf")
            
            
#             _mx = max(_mx, jobDifficulty[i])
#             return min(dp(i + 1, d, _mx), _mx + dp(i + 1, d - 1, 0))
    
#         return dp(0, d, 0)
        @cache
        def dp(i, day):
            if day == d: return max(jobDifficulty[i:])
            ans, curMax = float("inf"), 0
            for j in range(i, len(jobDifficulty) - d + day):
                curMax = max(curMax, jobDifficulty[j])
                ans = min(ans, curMax + dp(j + 1, day + 1))
            return ans
        
        return dp(0, 1)