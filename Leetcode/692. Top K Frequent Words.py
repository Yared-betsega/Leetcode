import heapq as hq
class Solution:
    def topKFrequent(self, words: List[int], k: int) -> List[int]:
        repo = Counter(words).items()
        repo = list(repo)
        for i in range(len(repo)):
            repo[i] = -1 * repo[i][1], repo[i][0]
            
        hq.heapify(repo)
        
        answer = []
        for i in range(k):
            seq = hq.heappop(repo)
            answer.append(seq[1])
        return answer

# space time complexity
# time complexity = O( n + klog(n) )
# space complexity O(1)
