class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid == 0:
                return nums[mid]
            elif nums[mid] == nums[mid-1]:
                if right - left == 1 and nums[left] != nums[right]:
                    return nums[right]
                elif (mid + 1) % 2 == 0:
                    left = mid + 1
                else: 
                    right = mid
            else:
                if nums[mid] != nums[mid+1]:
                    return nums[mid]
                elif (len(nums) - mid) % 2 == 0:
                    right = mid
                else:
                    left = mid + 1
                    
        return nums[right]
    
# time and space complexity
# time complexity = O(log(n))
# space complexity = O(1)
