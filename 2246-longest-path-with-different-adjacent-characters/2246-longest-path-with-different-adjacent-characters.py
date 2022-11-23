class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        graph = defaultdict(set)
        for i in range(len(parent)):
            graph[parent[i]].add(i)
        
        
        answer = [1]
        def dfs(node):
            
            if not graph[node]:
                return 1, node
            
            children = []
            for neigh in graph[node]:
                path, ch = dfs(neigh)
                if s[node] != s[ch]:
                    heappush(children, -path)
            
            i = 0
            pathSum = 0
            maxChild = -children[0] if children else 0
            while children and i < 2:
                pathSum += -heappop(children)
                i += 1
            answer[0] = max(answer[0], 1 + pathSum)
                        
            return maxChild + 1, node
        
        dfs(0)
        return answer[0]
                