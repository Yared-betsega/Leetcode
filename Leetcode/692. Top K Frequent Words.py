import heapq as hq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hq.heapify(words)
        repo = {}
        while words:
            value = hq.heappop(words)
            if value in repo:
                repo[value] += 1
            else:
                repo[value] = 1
        sortedNums = sorted(repo.items(), key = lambda x:x[1], reverse = True)
        return [x[0] for x in sortedNums[:k]]
                
