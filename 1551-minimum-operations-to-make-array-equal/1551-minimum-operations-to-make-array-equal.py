class Solution:
    def minOperations(self, n: int) -> int:
        target = None
        if n % 2 == 0:
            target = ((2 * (n // 2)) + 1 + ((2 * (n // 2 - 1))) + 1) // 2
        else:
            target = (2 * (n // 2)) + 1
        
        answer = 0
        for i in range(n // 2, n):
            answer += (2 * i + 1) - target
        return answer