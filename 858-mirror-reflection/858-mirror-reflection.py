class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)
        
        lcm = (p * q) / gcd(p, q)
        if (lcm / p) % 2 == 0:
            return 0
        if (lcm / q) % 2 == 0:
            return 2
        else: 
            return 1