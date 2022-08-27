class Solution:
    def helper(self, nums, left, right):
        if right - left + 1 < 3:
            return 
        mid = (left + right) // 2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        else:
            lst = [self.helper(nums, left, mid-1), self.helper(nums, mid, right)]
            if lst[0] == None:
                return lst[1]
            else:
                return lst[0]
            
        
    def findPeakElement(self, nums: List[int]) -> int:
        answer = self.helper(nums, 0, len(nums)-1)
        if answer != None:
            return answer
        return nums.index(max(nums))
        
# time and space complexity
# time complexity = O(n)
# space complexity = O(1)