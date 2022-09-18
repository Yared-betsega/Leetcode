class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 0:
            heap = [(1, (0,0))]
        else: return -1
        
        DIR = [(-1,0), (1,0), (0,1), (0,-1), (1, 1), (-1, 1), (1,-1), (-1,-1)]
        visited = set([(0, 0)])
        isValid = lambda tup: 0<=tup[0]<n and 0<=tup[1]<n
        while heap:
            path, coord = heappop(heap)
            if coord == (n-1, n-1):
                return path
            for direction in DIR:
                neighbor = (coord[0]+direction[0], coord[1]+direction[1])
                if isValid(neighbor) and grid[neighbor[0]][neighbor[1]] == 0:
                    if neighbor not in visited:
                        heappush(heap, (path + 1, neighbor))
                        visited.add(neighbor)
        
        return -1

            