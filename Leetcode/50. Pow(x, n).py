class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n % 2 == 0:
            if n < 0:
                return self.myPow(x, n//2) ** 2
            return  self.myPow(x, n//2) ** 2
        if n < 0:
            return (1/x) * self.myPow(x, n+1)
        return x * self.myPow(x, n-1)
