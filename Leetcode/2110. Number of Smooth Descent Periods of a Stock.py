# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = total = 1
        for i in range(1, len(prices)):
            cur = dp + 1 if prices[i] == prices[i-1] - 1 else 1
            dp = cur
            total += cur
        return total

# time and space compexity 
# time complexity = O(n)
# space complexity = O(1)
