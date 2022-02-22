import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hq.heapify(nums)
        repo = {}
        while nums:
            value = hq.heappop(nums)
            if value in repo:
                repo[value] += 1
            else:
                repo[value] = 1
        sortedNums = sorted(repo.items(), key = lambda x:x[1], reverse = True)
        return [x[0] for x in sortedNums[:k]]
                
