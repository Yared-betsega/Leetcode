class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def choose(i):
            if i >= len(nums):
                return 0
            return max(choose(i + 1), nums[i] + choose(i + 2))
        return choose(0)

# time and space complexity
# time complexity = O(n ** 2)
# space complexity = O(n)
                
                