
def checkArithmeticSubarrays(nums, l, r):
    def arthimeticSubarray(nums):
        nums = sorted(nums, reverse= True)
        min = nums[0]
        max = nums[1]
        difference = max - min
        for i in nums[1:]:
            max = i
            diff = max - min
            if diff != difference:
                return False
            min = max
        return True
      
    ans = []
    for i in range(len(l)):
        lst = nums[l[i]:r[i] +  1]
        ans.append(arthimeticSubarray(lst))
        
    return ans
