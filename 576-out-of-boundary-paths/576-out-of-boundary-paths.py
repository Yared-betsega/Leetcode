class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        outOfBound = lambda x: not 0<=x[0]<m or not 0<=x[1]<n
        DIR = [(1,0), (-1,0),(0,1),(0,-1)]
        @cache
        def dp(r, c, moves):
            if outOfBound((r, c)): return 1
            if moves == 0: return 0
            ans = 0
            for dx, dy in DIR:
                nx, ny = r + dx, c + dy
                ans += dp(nx, ny, moves - 1)
            
            return ans
        
        return dp(startRow, startColumn, maxMove) % (10 ** 9 + 7)
                