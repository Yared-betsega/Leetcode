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
                    children.append(path)
            
            if len(children) <= 2:
                answer[0] = max(answer[0], 1 + sum(children))
            
            else:
                children.sort()
                answer[0] = max(answer[0], 1 + children[-1] + children[-2])
            children.append(0)
            return max(children) + 1, node
        
        dfs(0)
        return answer[0]
                