class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                _max = i + 1
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i] and nums[j] <= nums[_max]:
                        _max = j
                nums[i], nums[_max] = nums[_max], nums[i]
                l, r = i + 1, len(nums) - 1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                found = True
                break
                        
        if not found:
            nums.sort()

# time and space complexity
# time: O(n)
# space: O(1)
            