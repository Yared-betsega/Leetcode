class Solution:
    def climbStairs(self, n: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        dp[1] = 1
        
        if n in dp:
            return dp[n]
        
        for i in range(2, n+1):
            temp = 0
            for j in range(1, 3):
                temp += (dp[i-j])
            dp[i] = temp
        
        return dp[n]

# time and space complexity
# time complexity = O(n)
# space complexity =O(n)
