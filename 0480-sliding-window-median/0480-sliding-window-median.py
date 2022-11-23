class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxHeap, minHeap = [], []
        for i in range(k):
            if len(maxHeap) >= len(minHeap):
                heappush(maxHeap, -nums[i])
                heappush(minHeap, -heappop(maxHeap))
            else:
                heappush(minHeap, nums[i])
                heappush(maxHeap, -heappop(minHeap))
        
        answer = []
        if len(minHeap) == len(maxHeap):
            answer.append((minHeap[0] - maxHeap[0]) / 2)
        else:
            answer.append(minHeap[0])
            
        for i in range(k, len(nums)):
            if nums[i - k] in minHeap:
                minHeap.remove(nums[i - k])
                heapify(minHeap)
            else: 
                maxHeap.remove(-nums[i - k])
                heapify(maxHeap)
            
            if len(maxHeap) >= len(minHeap):
                heappush(maxHeap, -nums[i])
                heappush(minHeap, -heappop(maxHeap))
            else:
                heappush(minHeap, nums[i])
                heappush(maxHeap, -heappop(minHeap))
                
            if len(minHeap) == len(maxHeap):
                answer.append((minHeap[0] - maxHeap[0]) / 2)
            else:
                answer.append(minHeap[0])
        return answer
            