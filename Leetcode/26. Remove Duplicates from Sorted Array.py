class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 0
        k=0
        while i < len(nums):
            if nums[i] != nums[j]:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j+=1
            else:
                k+=1
            i+=1
            
        return len(nums) - k
