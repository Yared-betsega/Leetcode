class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = r = 0
        while r < len(nums):
            if nums[l] == 0:
                while r < len(nums) and nums[r] == 0:
                    r += 1
                if r == len(nums):
                    break
                nums[l], nums[r] = nums[r], nums[l]
                
                l += 1
            else:
                l += 1
                r += 1
            
#         i , j = 0 , 1
#         while i < len(nums):
#             if nums[i] == 0:
#                 nums.pop(i)
#                 nums.append(0)
#                 if j >= len(nums):
#                     break
#                 j+=1
#                 continue
#             i+=1
#             j+=1
                
        