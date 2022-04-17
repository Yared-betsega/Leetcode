# https://leetcode.com/problems/min-cost-to-connect-all-points/


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find_set(i):
            if i == parent[i]:
                return i
            parent[i] = find_set(parent[i])
            return parent[i]
        
        def union_sets(i, j):
            a = find_set(i)
            b = find_set(j)
            if a!=b:
                if size[a] >= size[b]:
                    parent[b] = a
                    size[a] += size[b]
                else:
                    parent[a] = b
                    size[b] += size[a]

        graph = []
        parent, size = {}, {}
        for i in range(len(points)):
            fir = tuple(points[i])
            parent[fir] = fir
            size[fir] = 1
            for j in range(i+1, len(points)):
                sec = tuple(points[j])
                if fir != sec:
                    man = abs(fir[0]-sec[0]) + abs(fir[1]-sec[1])
                    graph.append([man, (fir, sec)])
        graph.sort()
        ans = 0
        i=0
        while i<len(graph):
            man, cur = graph[i]
            a = find_set(cur[0])
            b = find_set(cur[1])
            if a!=b:
                ans += man
                union_sets(a, b)
            i+=1
                
        return ans
