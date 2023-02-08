class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b in adjacentPairs:
            graph[a].add(b)
            graph[b].add(a)
            
        def dfs(element):
            visited.add(element)
            res.append(element)
            for neigh in graph[element]:
                if neigh not in visited:
                    dfs(neigh)
        
        visited = set()
        res = []
        for elem in graph:
            if len(graph[elem]) == 1:
                dfs(elem)
                break
        
        return res