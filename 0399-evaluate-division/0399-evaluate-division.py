class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        N = len(equations)
        for i in range(N):
            graph[equations[i][0]][equations[i][1]] = values[i] 
            graph[equations[i][1]][equations[i][0]] = 1/values[i] 
        
        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1
            if y in graph[x]:
                return graph[x][y]
            
            visited.add(x)
            for node in graph[x]:
                if node not in visited:
                    val = dfs(node, y, visited)
                    if val != -1:
                        return val * graph[x][node]

            return -1
        
        ans = []
        for x, y in queries:
            ans.append(dfs(x, y, set()))
        
        return ans