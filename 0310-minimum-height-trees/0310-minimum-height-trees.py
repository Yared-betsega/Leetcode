class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            indegree[node1] += 1
            indegree[node2] += 1
        
        visited = set()
        queue = deque()
        for node in indegree:
            if indegree[node] == 1:
                queue.append(node)
                indegree[node] -= 1

        answer = []
        while queue:
            if len(visited) == n - 1 or len(visited) == n - 2:
                return queue
            for i in range(len(queue)):
                currentNode = queue.popleft()
                visited.add(currentNode)
                for neighbor in graph[currentNode]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        queue.append(neighbor)
    
            