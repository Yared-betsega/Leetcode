class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        pref = piles[:]
        for pile in pref:
            for i in range(1, len(pile)):
                pile[i] = pile[i] + pile[i - 1]
        @cache
        def dp(i, k):
            if k <= 0 or i >= len(piles):
                return 0
            _max = dp(i + 1, k)
            n = len(pref[i])
            for j in range(min(k, n)):
                _max = max(_max,  pref[i][j] + dp(i + 1, k - (j + 1) ))
            return _max
        return dp(0, k)
            
            