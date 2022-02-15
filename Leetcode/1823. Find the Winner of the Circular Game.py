class Solution:
    def helper(self, k, sequence, current):
        if len(sequence) == 1:
            return sequence[0]
        current = current - 1 + k
        while current > len(sequence) - 1:
            current -= len(sequence)
        sequence.pop(current)
        return self.helper(k, sequence, current)
    
    def findTheWinner(self, n: int, k: int) -> int:
        sequence = [i for i in range(1, n+1)]
        return self.helper(k, sequence, 0)
