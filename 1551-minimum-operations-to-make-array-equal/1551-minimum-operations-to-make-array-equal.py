class Solution:
    def minOperations(self, n: int) -> int:
        return  (n // 2) ** 2 if n % 2 == 0 else ((n // 2) ** 2) + (n // 2)        
    
# time and space complexity
# time: O(1)
# space: O(1)