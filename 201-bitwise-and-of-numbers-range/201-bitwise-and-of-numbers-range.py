class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        maxBinLength = len(bin(right)[2:])
        ans = cur = 0
        for i in range(maxBinLength - 1, -1, -1):
            if right & (1 << i):
                cur += (1 << i)
                if left >= cur:
                    ans += (1 << i)
        return ans
                