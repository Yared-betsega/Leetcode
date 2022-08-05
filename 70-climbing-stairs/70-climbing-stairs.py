class Solution:
    def climbStairs(self, n: int) -> int:
        # DP bottom up implementation
        dp = defaultdict(int)
        oneStep, twoStep = 1, 1
        if n < 2:
            return 1
        for i in range(2, n+1):
            temp = oneStep + twoStep
            oneStep = twoStep
            twoStep = temp
            
        return twoStep

# time and space complexity
# time complexity = O(n)
# space complexity =O(1)