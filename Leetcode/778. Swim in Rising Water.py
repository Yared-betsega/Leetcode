import heapq as hq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def isValid(tup):
            return True if 0<=tup[0]<len(grid) and 0<=tup[1]<len(grid) and tup not in self.visited else False
        
        self.DIR = [[-1,0], [1,0], [0,1], [0,-1]]
        self.visited = set()
        self.maxim = -float("inf")
        
        def bfs(cord):
            heap = []
            hq.heappush(heap, [grid[cord[0]][cord[1]], cord])
            
            
            while heap:
              
                current = hq.heappop(heap)
                self.visited.add(current[1])
                self.maxim = max(self.maxim, current[0])
                
                for tup in self.DIR:
                    neighbor = (current[1][0]+tup[0], current[1][1]+tup[1])
                    
                    if isValid(neighbor):
                        if neighbor == (len(grid)-1, len(grid)-1):
                            return max(self.maxim, grid[-1][-1])
                        hq.heappush(heap, [grid[neighbor[0]][neighbor[1]], neighbor])
        
        return bfs((0,0)) if len(grid) > 1 else 0

# time and space complexity 
# time complexity = O(nlog(n))
# space complexity = O(n)
                
            
            
