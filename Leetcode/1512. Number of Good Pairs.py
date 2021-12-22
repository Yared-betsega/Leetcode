def numIdenticalPairs(nums):
    length = len(nums)
    counter = 0
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] == nums[j]:
                counter += 1
    return counter
