def topKFrequent(nums, k):
    nums = sorted(nums)
    uniques = set(nums)
    uniques = list(uniques)
    eachCount = {}
    ans = []
    for i in uniques:
        rep = nums.count(i)
        eachCount[i] = rep
    sortedCount = sorted(eachCount.items(), key= lambda x:x[1], reverse=True)
    ans = [x[0] for x in sortedCount[:k]]
    return ans
