class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = zeros = 0
        zeroOne = oneZero = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "0":
                zeros += 1
                oneZero += ones
                ans += zeroOne
            else:
                ones += 1
                zeroOne += zeros
                ans += oneZero
        
        return ans