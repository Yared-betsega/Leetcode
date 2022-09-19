class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
            
            elif nums[nums[i] - 1] == nums[i]:
                i += 1
            else:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]
        ans = []
        for i, val in enumerate(nums):
            if i + 1 != nums[i]:
                ans.append(i + 1)
        return ans
            
        
        print(nums)