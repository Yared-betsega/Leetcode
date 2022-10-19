class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        prefix = defaultdict(int)
        minElement = float("inf")
        maxElement = -float("inf")
        for left, right in intervals:
            prefix[left] += 1
            prefix[right + 1] -= 1
            minElement = min(minElement, left, right)
            maxElement = max(maxElement, left, right)
            
        
        total = 0
        answer = 0
        for i in range(minElement, maxElement + 1):
            total += prefix[i]
            answer = max(total, answer)
        
        return answer
            