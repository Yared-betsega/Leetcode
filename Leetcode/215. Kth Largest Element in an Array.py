import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            hq.heappush(heap, -1 * nums[i])
        for i in range(k-1):
            hq.heappop(heap)
            
        return -1 * hq.heappop(heap)
      
#       space time complexity
#       time complexity = O(n + klog(n))
#       space complexity = O(n)
