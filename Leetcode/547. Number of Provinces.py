class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # Union Find Solution
        def find_set(i):
            if i == parent[i]:
                return i
            parent[i] = find_set(parent[i])
            return parent[i]
        
        def union_sets(i, j):
            a = find_set(i)
            b = find_set(j)
            if a!=b:
                if size[a] >= size[b]:
                    parent[b] = a
                    size[a] += size[b]
                else:
                    parent[a] = b
                    size[b] += size[a]
        
        parent, size = {}, {}
        for i in range(len(isConnected)):
            parent[i] = i
            size[i] = 1    
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union_sets(i, j)
                    
        count = 0
        for k, v in parent.items():
            if k == v:
                count += 1
        return count
    
#For union find Solution              
# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
        
        
        # DFS solution
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
                
            
