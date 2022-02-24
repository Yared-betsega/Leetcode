import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            hq.heappush(heap, -1 * stone)
        while len(heap) > 1:
            first = -1 * hq.heappop(heap)
            second = -1 * hq.heappop(heap)
            val = first - second
            if val > 0:
                hq.heappush(heap, -1 * val)
        if len(heap) == 0:
            return 0
        return -1 * heap[0]
        
