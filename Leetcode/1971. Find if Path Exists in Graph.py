class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        network = defaultdict(list)
        for val in edges:
            network[val[0]].append(val[1])
            network[val[1]].append(val[0])
        
        def bfs(source):
            visited = set()
            queue = deque([source])
            visited.add(source)
            while queue:
                cur = queue.popleft()
                if cur == destination:
                    return True
                
                for i in network[cur]:
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
                        
            return False
        
        return bfs(source)
