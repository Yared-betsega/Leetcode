def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if int(str(nums[j]) + str(nums[i])) > int(str(nums[i]) + str(nums[j])):
                    nums[i], nums[j] = nums[j], nums[i]
        return "".join(list(map(str, nums)))
