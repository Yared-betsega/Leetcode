class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # Sorting solution
        points.sort(key = lambda x:x[1])
        cnt = 1
        cur = points[0]
        for i in range(1, len(points)):
            if points[i][0] > cur[1]:
                cnt += 1
                cur = points[i]
        
        return cnt
      
        # Heap Solution
        heap = []
        for point in points:
            hq.heappush(heap, (point[1], point[0]))
        
        cur = hq.heappop(heap)
        cnt = 1
        while heap:
            temp = hq.heappop(heap)
            if temp[1] > cur[0]:
                cnt += 1
                cur = temp           
            
        return cnt

# time and space complexity 
# time complexity = O(n)
# space complexity =O(1)
            
            
        
