
# https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            minim = maxim = nums[i]
            for j in range(i+1, len(nums)):
                minim = min(minim, nums[j])
                maxim = max(maxim, nums[j])
                total += maxim - minim
        
        return total

# time and space complexity
# time complexity = O(n**2)
# space complexity = O(1)
