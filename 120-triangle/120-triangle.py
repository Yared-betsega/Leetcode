class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def getMin(idx, arrIdx, memo):
            
            if arrIdx >= len(triangle):
                return 0
            
            if (idx, arrIdx) in memo:
                return memo[(idx, arrIdx)]
            
            ans = min(getMin(idx, arrIdx+1, memo), getMin(idx+1, arrIdx+1, memo))
            memo[(idx, arrIdx)] = triangle[arrIdx][idx] + ans

            return memo[(idx, arrIdx)]
        
        return getMin(0, 0 ,  {})

# time and space complexity 
# time comlexity = O(n)
# space complexity = O(n)