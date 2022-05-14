# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot = 0 
        real = 0
        for i in range(1, len(nums)+1):
            tot ^= nums[i-1]
            real ^= i
        return real ^ tot
    
# time complexity = O(n)
# space complexity = O(1)
