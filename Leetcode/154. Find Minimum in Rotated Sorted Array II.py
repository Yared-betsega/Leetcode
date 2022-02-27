class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] < nums[mid]:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[left] == nums[mid]:
                    if nums[mid] < nums[right]:
                        right = mid
                    elif nums[mid] > nums[right]:
                        left = mid + 1
                    else:
                        return min(self.findMin(nums[left:mid+1]), self.findMin(nums[mid+1:right+1]))
                else:
                    right = mid
                
        return nums[right]

# time and space complexity
# time complexity O(n)
# space complexity = O(n)
                    
            
