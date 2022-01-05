def minPairSum(nums):
  
    nums = sorted(nums)
    minimizedPair = []
    while len(nums) > 0:
        minimizedPair.append([nums[0], nums[-1]])
        nums.pop()
        nums.pop(0)
        
    listOfMaxes = list(map(lambda pair:pair[0] + pair[1], minimizedPair))
    
    return max(listOfMaxes)
