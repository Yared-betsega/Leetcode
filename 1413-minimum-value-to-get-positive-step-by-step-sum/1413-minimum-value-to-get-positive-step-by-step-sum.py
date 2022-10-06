class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0 
        startValue = 1
        for val in nums:
            prefix_sum += val
            if prefix_sum <= 0:
                startValue = max(startValue, 1 - prefix_sum)
        
        return startValue
  
# time and space complexity
# time: O(n)
# space: O(1)