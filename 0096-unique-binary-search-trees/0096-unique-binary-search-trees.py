class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def dp(left, right):
            if left >= right:
                return 1
            noOfSubtrees = 0
            for i in range(left, right + 1):
                noOfSubtrees += dp(left, i - 1) * dp(i + 1, right)
            return noOfSubtrees
        
        return dp(1, n)
            