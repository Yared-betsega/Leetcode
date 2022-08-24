class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        def rec(n):
            if n <= 5:
                return True
            if n & 1 == 0:
                return rec(n >> 1)
            elif n % 3 == 0:
                return rec(n // 3)
            elif n % 5 == 0:
                return rec(n // 5)
            return False
        
        return rec(abs(n))