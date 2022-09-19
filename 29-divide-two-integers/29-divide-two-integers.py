class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dsor = divisor if divisor > 0 else -divisor
        dned = dividend if dividend > 0 else -dividend
        if dned < dsor:
            return 0
        ans = 1
        quotient = 1
        while dsor <= dned:
            if (dsor << 1) <= dned:
                dsor <<= 1
                ans += quotient
                quotient += quotient

            elif dned - dsor < (divisor if divisor > 0 else -divisor):
                break
            else: 
                dned -= dsor
                dsor = divisor if divisor > 0 else -divisor
                quotient = 1
                ans += quotient
        ans = -ans if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0 else ans
        if ans < -(1 << 31):
            return -(1 << 31)
        if ans > (1 << 31) - 1:
            return (1 << 31) - 1
        return ans
        
            
            