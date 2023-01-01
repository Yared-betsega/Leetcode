class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
      
        
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
            
        visited = set()
        answer = [-float("inf")]
        def dfs(node, parentVal):
            if not graph[node] or node in visited:
                answer[0] = max(answer[0], vals[node])
                return vals[node]
            visited.add(node)
            starGraph = []
            for child in graph[node]:
                heappush(starGraph, -dfs(child, vals[node]))
            i = 0
            starSum = vals[node]
            while i < k and starGraph:
                starSum += -heappop(starGraph)
                i += 1
                answer[0] = max(answer[0], starSum)
            return vals[node]
        
        for node in range(len(vals)):
            dfs(node, 0)
        return answer[0]