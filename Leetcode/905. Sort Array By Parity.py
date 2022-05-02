# https://leetcode.com/problems/sort-array-by-parity/

  class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [num for num in nums if num % 2 == 0] + [num for num in nums if num % 2 != 0]
    
# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
