def rearrangeArray(nums):
        nums = sorted(nums)
        center = len(nums)//2 if len(nums) % 2 != 0 else len(nums)//2 - 1
        ans = []
        ans.extend(nums[:center+1])
        aboveCenter = nums[center+1:]

        if len(nums) % 2 == 0:
            even = 0
            while len(aboveCenter) > 0:
                ans.insert(even, aboveCenter[-1])
                aboveCenter.pop()
                even += 2
        else:
            odd = 1
            while len(aboveCenter) > 0:
                ans.insert(odd, aboveCenter[-1])
                aboveCenter.pop()
                odd += 2
        return ans
