class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxPos = 0
        for i in range(24):
            ones = 0
            for candidate in candidates:
                if 1 << i & candidate:
                    ones += 1
            maxPos = max(maxPos, ones)
            
        return maxPos