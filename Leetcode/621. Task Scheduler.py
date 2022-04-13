# https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        heap = []
        for cnt in count.values():
            heapq.heappush(heap, -1 * cnt)
        
        currentTime = 0
        queue = deque()
        
        while heap or queue:
            currentTime += 1
            if heap:
                cur = heapq.heappop(heap) + 1
                if cur:
                    queue.append((cur, currentTime + n))
            
            if queue and queue[0][1] == currentTime:
                heapq.heappush(heap, queue.popleft()[0])
            
        return currentTime
                
            
            
            
        
    
                
                
        
