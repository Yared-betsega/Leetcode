class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)
        for u, v, w in times:
            graph[u].add((v, w))
        
        answer = 0
        distanceToLast = [float("inf")] * (n + 1)
        distanceToLast[k] = 0
        distanceToLast[0] = 0
        heap = [(0, k)]  
        while heap:
            tillNow, currentNode = heappop(heap)
            for neighbor, weight in graph[currentNode]:
                distanceToNeighbor = tillNow + weight
                if distanceToNeighbor < distanceToLast[neighbor]:
                    distanceToLast[neighbor] = distanceToNeighbor
                    heappush(heap, (distanceToNeighbor, neighbor))
        
        if float("inf") in distanceToLast:
            return -1
        return max(distanceToLast)
                    
        