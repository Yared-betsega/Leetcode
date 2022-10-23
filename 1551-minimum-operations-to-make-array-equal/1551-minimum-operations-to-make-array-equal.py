class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n // 2) ** 2            
        else:
            return ((n // 2) ** 2) + (n // 2)
        
        
    
# time and space complexity
# time: O(1)
# space: O(1)