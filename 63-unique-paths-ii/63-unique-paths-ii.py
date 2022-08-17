class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # DP top-down solution with both @lru_catch and manual memoization
        DIR = [(0, 1), (1, 0)]
        isValid = lambda move: 0 <= move[0] < len(obstacleGrid) and 0 <= move[1] < len(obstacleGrid[0])
        
        @lru_cache
        def dfs(node):
            if not isValid(node) or obstacleGrid[node[0]][node[1]] == 1:
                return 0
            elif node == (len(obstacleGrid)-1, len(obstacleGrid[0])-1):
                return 1

            rnxt = (node[0]+0, node[1]+1)
            bnxt = (node[0]+1, node[1]+0)
            return dfs(rnxt) + dfs(bnxt)
 
        return dfs((0, 0))


# time O(mn)
# space = O(mn)

        