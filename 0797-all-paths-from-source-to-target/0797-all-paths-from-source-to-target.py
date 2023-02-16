class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(node, path):
            if node == len(graph) - 1:
                ans.append(path[:])
            else:
                for neigh in graph[node]:
                    path.append(neigh)
                    dfs(neigh, path)
                    path.pop()
        
        dfs(0, [0])
        return ans