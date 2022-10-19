class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v, weight in edges:
            graph[u].add((v, weight))
            graph[v].add((u, weight))
        
        distanceToLastNode = self.findShortestPath(graph, n)
        directedAcyclicGraph = defaultdict(set)
        for u, v, weight in edges:
            if distanceToLastNode[u] > distanceToLastNode[v]:
                directedAcyclicGraph[u].add((v))
            elif distanceToLastNode[v] > distanceToLastNode[u]:
                directedAcyclicGraph[v].add((u))
        @cache
        def dp(node):
            if node == n:
                return 1
            answer = 0
            for neighbor in directedAcyclicGraph[node]:
                answer += dp(neighbor)
            return answer
        
        return dp(1) % (10 ** 9 + 7)
    
    def findShortestPath(self, graph, lastNode):
        """
        Apply dijkstra's algorithm to find the shortest distance from 
        each node to the last node
        """ 
        distanceToLastNode = [float("inf")] * (lastNode + 1)
        distanceToLastNode[-1] = 0
        heap = [(0, lastNode)]
        while heap:
            weightTillNow, currentNode = heappop(heap)
            for nextNode, weight in graph[currentNode]:
                pathToNode = weight + weightTillNow
                if pathToNode < distanceToLastNode[nextNode]:
                    distanceToLastNode[nextNode] = pathToNode
                    heappush(heap, (pathToNode, nextNode))
        
        return distanceToLastNode
        