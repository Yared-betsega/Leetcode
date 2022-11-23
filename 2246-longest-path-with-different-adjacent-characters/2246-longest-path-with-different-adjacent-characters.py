class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(set)
        for i in range(len(parent)):
            graph[parent[i]].add(i)
        
        
        answer = [1]
        def dfs(node):
            
            if not graph[node]:
                return 1, node
            
            pathsFromChildren = []
            for neigh in graph[node]:
                path, ch = dfs(neigh)
                if s[node] != s[ch]:
                    heappush(pathsFromChildren, -path)
            
            i = 0
            pathSumForTwoBranches = 0
            maxChildPath = -pathsFromChildren[0] if pathsFromChildren else 0
            while pathsFromChildren and i < 2:
                pathSumForTwoBranches += -heappop(pathsFromChildren)
                i += 1
            answer[0] = max(answer[0], 1 + pathSumForTwoBranches)
                        
            return maxChildPath + 1, node
        
        dfs(0)
        return answer[0]
                