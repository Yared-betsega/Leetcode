class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def markConnected(city, visited):
            visited.add(city)
            for i in range(len(isConnected)):
                if i not in visited and isConnected[i][city] == 1:
                    markConnected(i, visited)
        
        visited = set()
        provinces = 0
        for city in range(len(isConnected)):
            if city not in visited:
                provinces += 1
                markConnected(city, visited)
                
        return provinces
                
            
