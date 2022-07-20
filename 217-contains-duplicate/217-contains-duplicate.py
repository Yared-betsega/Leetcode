class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# time and space complexity
# time: O(n)
# space: O(n)