class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                count = 1
                cur = num
                while cur + 1 in nums:
                    count += 1
                    cur = cur + 1
                longest = max(longest, count)
        
        return longest

# time and space complexity 
# time complexity = O(n)
# space complexity = O(1)
