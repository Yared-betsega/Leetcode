class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        isValid = lambda x: 0 <= x[0] < m and 0 <= x[1] < n
        @cache
        def dp(r, c):
            if isValid((r, c)):
                if r == m - 1 and c == n - 1:
                    if dungeon[r][c] <= 0:
                        return dungeon[r][c]
                    return 0
                after = dungeon[r][c] +  max(dp(r + 1, c), dp(r, c + 1))
                if after <= 0:
                    return after
                return 0
            return -float("inf")
        # print(dp(0, 0))
        ans = -dp(0, 0) + 1
        return ans if ans != float("inf") else 1
        