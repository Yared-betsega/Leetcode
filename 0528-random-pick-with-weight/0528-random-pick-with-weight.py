class Solution:

    def __init__(self, w: List[int]):
        self.probDistribution = [0] * len(w)
        _sum = 0
        for i in range(len(w)):
            _sum += w[i]
            self.probDistribution[i] = _sum
        
        # print(self.probDistribution)
        
    def pickIndex(self) -> int:
        return bisect_left(self.probDistribution, random.randint(1, self.probDistribution[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()