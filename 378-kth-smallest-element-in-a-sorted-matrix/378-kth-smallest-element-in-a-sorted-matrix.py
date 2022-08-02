import heapq as hq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        hq.heapify(matrix)
        
        for i in range(k - 1):
            ls = hq.heappop(matrix)
            ls.pop(0)
            if ls:
                hq.heappush(matrix, ls)
        
        return hq.heappop(matrix)[0]
            
# time and space complexity
# time complexity = O(n + k)
# space complexity = O(1)