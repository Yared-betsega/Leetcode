class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        isValid = lambda x: 0 <= x[0] < m and 0 <= x[1] < n
        
        # Top down solution
        # @cache
        # def dp(r, c):
        #     if isValid((r, c)):
        #         if r == m - 1 and c == n - 1:
        #             if dungeon[r][c] <= 0:
        #                 return dungeon[r][c]
        #             return 0
        #         after = dungeon[r][c] +  max(dp(r + 1, c), dp(r, c + 1))
        #         if after <= 0:
        #             return after
        #         return 0
        #     return -float("inf")
        # ans = -dp(0, 0) + 1
        # return ans if ans != float("inf") else 1
        
# time and space complexity
# time: O(mn)
# space: O(mn)

        # Bottom up solution
        dp = [[-float("inf")] * n for i in range(m)]
        dp[m - 1][n - 1] = dungeon[m-1][n-1] if dungeon[m-1][n-1] < 0 else 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                right = dp[i + 1][j] if isValid((i + 1, j)) else -float("inf")
                bottom = dp[i][j + 1] if isValid((i, j + 1)) else -float("inf")  
                ans = dungeon[i][j] + max(right, bottom)
                if ans == -float("inf"):
                    if dungeon[i][j] <= 0:
                        dp[i][j] = dungeon[i][j]
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = ans  if ans <= 0 else 0
        return -dp[0][0] + 1

# time and space complexity
# time: O(mn)
# space: O(mn)