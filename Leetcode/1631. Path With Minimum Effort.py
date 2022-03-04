import heapq as hq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def isValid(tup):
            return True if 0<=tup[0]<len(heights) and 0<=tup[1]<len(heights[0]) and tup not in self.visited else False
        
        self.DIR = [[-1,0], [1,0], [0,1], [0,-1]]
        self.visited = set()
     
        heap = []
        hq.heappush(heap, (0, (0, 0)))
        self.visited.add((0, 0))
        maxim = -float("inf")
        while heap:
          
            current = hq.heappop(heap)
            self.visited.add(current[1])
            
            if current[0] > maxim:
                maxim = current[0]
                
            if current[1] == (len(heights) - 1, len(heights[0]) - 1):
                return maxim
            
            for tup in self.DIR:
                neighbor = (current[1][0]+tup[0], current[1][1]+tup[1])
                if isValid(neighbor):
                    absDif = abs(heights[neighbor[0]][neighbor[1]] - heights[current[1][0]][current[1][1]])
                    hq.heappush(heap,(absDif, neighbor))
                    
        return maxim
            
