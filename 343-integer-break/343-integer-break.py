class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        @cache
        def helper(n):
            if n == 1 or n == 3 or n == 2:
                return n
            ans = 0
            for i in range(1, n):
                ans = max(ans, i * helper(n - i))
            return ans
        return helper(n)