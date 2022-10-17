class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        @cache
        def dp(i, d, _mx):
            if i >= len(jobDifficulty):
                if not d: return _mx
                else: return float("inf")     
            if d < 0: return float("inf")
            
            
            _mx = max(_mx, jobDifficulty[i])
            return min(dp(i + 1, d, _mx), _mx + dp(i + 1, d - 1, 0))
    
        return dp(0, d, 0)