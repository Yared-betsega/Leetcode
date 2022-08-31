class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         for i in range(k % len(nums)):
#             temp = nums.pop()
#             nums.insert(0, temp)
            
#         # time space Complexity
#         # time complexity = O(nk), n = len(nums)
#         # space complexity = O(1)
        
        k %= len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1
        return nums
            
        