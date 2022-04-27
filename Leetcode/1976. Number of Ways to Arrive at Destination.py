# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
            
        heap = [(0,0)]
        shortest_time_to_reach_here = [float("inf")] * (n)
        shortest_time_to_reach_here[0] = 0
        ways_to_reach_here = [0] * (n)
        ways_to_reach_here[0] = 1
        
        while heap:
            tot, u = heapq.heappop(heap)
            
            for v, time_from_parent in graph[u]:
                time_to_here = tot + time_from_parent
                if time_to_here < shortest_time_to_reach_here[v]:
                    heapq.heappush(heap, (time_to_here, v))
                    shortest_time_to_reach_here[v] = time_to_here
                    ways_to_reach_here[v] = ways_to_reach_here[u]
                elif time_to_here == shortest_time_to_reach_here[v]:
                    ways_to_reach_here[v] += ways_to_reach_here[u]

        return ways_to_reach_here[-1] % (10**9 +7)
            
