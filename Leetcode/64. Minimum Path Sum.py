# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # Dynamic Programming top-down Implementation
        
        def getMinPath(arrIdx, idx, memo):
            
            if not 0 <= arrIdx < len(grid) or not 0 <= idx < len(grid[arrIdx]):
                return float("inf")
            
            if (arrIdx, idx) == (len(grid) - 1, len(grid[-1]) - 1):
                return  grid[-1][-1]
            
            if (arrIdx, idx) in memo:
                return memo[arrIdx, idx]
            
            ans = grid[arrIdx][idx] + min(getMinPath(arrIdx+1, idx, memo), getMinPath(arrIdx, idx+1, memo))
            
            memo[arrIdx, idx] = ans
            
            return memo[arrIdx, idx]
    
        return getMinPath(0, 0, {})
    
# time and space complexity
# time complexity = O(nm)
# space complexity = O(nm)

            
        
