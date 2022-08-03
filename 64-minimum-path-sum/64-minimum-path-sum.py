class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
#         # Dynamic Programming top-down Implementation
        
#         def getMinPath(arrIdx, idx, memo):
            
#             if not 0 <= arrIdx < len(grid) or not 0 <= idx < len(grid[arrIdx]):
#                 return float("inf")
            
#             if (arrIdx, idx) == (len(grid) - 1, len(grid[-1]) - 1):
#                 return  grid[-1][-1]
            
#             if (arrIdx, idx) in memo:
#                 return memo[arrIdx, idx]
            
#             ans = grid[arrIdx][idx] + min(getMinPath(arrIdx+1, idx, memo), getMinPath(arrIdx, idx+1, memo))
            
#             memo[arrIdx, idx] = ans
            
#             return memo[arrIdx, idx]
    
#         return getMinPath(0, 0, {})

#         # time and space complexity
#         # time complexity = O(nm)
#         # space complexity = O(nm)

        # DP bottom up implementation
        is_valid = lambda x: 0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0])
        ans = [[ -1 for i in range(len(grid[0])) ] for j in range(len(grid))]

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if not is_valid((i + 1, j)) and not is_valid((i, j + 1)):
                    ans[i][j] = grid[i][j]
                elif is_valid((i + 1, j)) and is_valid((i, j + 1)):
                    ans[i][j] = grid[i][j] + min(ans[i+1][j], ans[i][j+1])
                elif is_valid((i + 1, j)):
                    ans[i][j] = grid[i][j] + ans[i+1][j]
                else: 
                    ans[i][j] = grid[i][j] + ans[i][j + 1]
        return ans[0][0]
        
        # time and space complexity
        # time complexity = O(nm)
        # space complexity = O(nm)