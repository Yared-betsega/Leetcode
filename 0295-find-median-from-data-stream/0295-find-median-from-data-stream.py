import heapq as hq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            
            hq.heappush(self.minHeap, num)
            hq.heappush(self.maxHeap, -heappop(self.minHeap))
        else:
            hq.heappush(self.maxHeap, -1 * num)
            hq.heappush(self.minHeap, -1 * hq.heappop(self.maxHeap))
        
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        first = -1 * self.maxHeap[0]
        second = self.minHeap[0]
        return (first + second) / 2


# time and space complexity
# time comlexity = O(log(n)) for both functions ( addNum and findMedian)
# space complexity = O(n) for both functions ( addNum and findMedian)