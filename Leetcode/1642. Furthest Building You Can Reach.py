import heapq as hq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i, heap = 1, []
        while i < len(heights):
            val = heights[i] - heights[i - 1]
            if val > 0:
                hq.heappush(heap, val)
                if ladders > 0:
                    ladders -= 1
                elif bricks >= heap[0]:
                    bricks -= hq.heappop(heap)
                else:
                    return i - 1
            i += 1
        return len(heights) - 1
            
# time and space complexity 
# time complexity = O(nlog(n))
# space complexity = O(n)
