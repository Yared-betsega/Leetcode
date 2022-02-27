class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else: 
                    right = mid
            else:
                right = mid
                
        return nums[right]

# time and space complexity
# time complexity = O(log(n))
# space complexity = O(1)
