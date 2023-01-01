class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return stones[1] - stones[0]
        difodd = 0
        for i in range(2, len(stones), 2):
            difodd = max(difodd, stones[i] - stones[i - 2])
        
        difEven = 0
        for i in range(1, len(stones), 2):
            difEven = max(difEven, stones[i] - stones[i - 2])
        return max(difodd, difEven)