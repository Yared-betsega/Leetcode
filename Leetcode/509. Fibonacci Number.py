class Solution:
    def fib(self, n: int, memo = {}) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        if n in memo:
            return memo[n]
        
        value = self.fib(n-1) + self.fib(n-2)
        memo[n] = value
        return value

# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
