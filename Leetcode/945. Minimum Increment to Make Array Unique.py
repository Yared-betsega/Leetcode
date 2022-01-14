def minIncrementForUnique(nums):
        nums = sorted(nums)
        cr = 0
        store = {}
        for i in range(len(nums)):
            if nums[i] in store:
                cr += nums[i-1] - nums[i] + 1
                nums[i] += (nums[i-1] - nums[i])+1
                store[nums[i]] = 1
            else:
                store[nums[i]] = 1
        return cr
