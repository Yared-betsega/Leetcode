class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        ans = [0] * n
        def dfs(node):
            visited.add(node)
            count = defaultdict(int)
            for nxt in graph[node]:
                if nxt not in visited:
                    subCount = dfs(nxt)
                    for k, v in subCount.items():
                        count[k] += subCount[k]
            count[labels[node]] += 1
            ans[node] += count[labels[node]]                
            return count
        visited = set()
        dfs(0)
        return ans