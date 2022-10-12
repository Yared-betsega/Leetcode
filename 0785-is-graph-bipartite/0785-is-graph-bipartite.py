class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = defaultdict(lambda : -1)
        def bfs(root):
            queue = deque([(root, 0)])
            color[root] = 0
            while queue:
                cur, clr = queue.popleft()
                color[cur] = clr
                for nxt in graph[cur]:
                    if color[cur] == color[nxt]:
                        return False
                    if color[nxt] == -1:
                        queue.append((nxt, 1 - color[cur]))
            return True
        
        for i in range(len(graph)):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True
                        