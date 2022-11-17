class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] == i + 1 or nums[nums[i] - 1] == nums[i]:
                i += 1
                continue
            cur = nums[i]
            nums[i], nums[cur - 1] = nums[cur - 1], nums[i]
            # print(nums)
            
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i], i + 1