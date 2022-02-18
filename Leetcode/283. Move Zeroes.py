class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i , j = 0 , 1
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                if j >= len(nums):
                    break
                j+=1
                continue
            i+=1
            j+=1
