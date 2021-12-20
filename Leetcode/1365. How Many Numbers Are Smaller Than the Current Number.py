class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        length = len(nums)
        for i in range(length):
            Counter = 0
            for j in range(length):
                if nums[i] > nums[j]:
                    Counter += 1
            ans.append(Counter)
        return ans