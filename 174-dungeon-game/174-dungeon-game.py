class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        isValid = lambda x: 0 <= x[0] < len(dungeon) and 0 <= x[1] < len(dungeon[0])
        @cache
        def dp(r, c, life):
            if isValid((r, c)):
                life += dungeon[r][c]
                if life <= 0:
                    return False
                if r == len(dungeon) - 1 and c == len(dungeon[0]) - 1:
                    return True
                return dp(r + 1, c, life) or dp(r, c + 1, life)
            return False
        
        m, n = len(dungeon), len(dungeon[0])
        l, r = 1, m * n * (1001)
        while l < r:
            m = (l + r) // 2
            if dp(0, 0, m):
                r = m
            else:
                l = m + 1
                
        return r
            