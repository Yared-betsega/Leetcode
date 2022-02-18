class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0
        
        for i in range(1, len(nums)):
            right += nums[i]
        if left == right:
            return 0
        
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i
            
        return -1

    # time space complexity
    # time complexity = O(n)
    # space complexity = O(1)
