class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            
        dis = {}
        queue = deque([(0, 0)])
        visited = set([0])
        while queue:
            cur, length = queue.popleft()
            dis[cur] = length * 2
            for nxt in graph[cur]:
                if nxt not in visited:
                    queue.append((nxt, length + 1))
                    visited.add(nxt)
        
        ans = -float("inf")
        for i in range(1, len(patience)):
            if patience[i] < dis[i]:
                rem = dis[i] % patience[i]
                lastCall = dis[i] - (rem) if rem > 0 else dis[i] - patience[i]
                ans = max(ans, lastCall + dis[i]) 
            else:
                ans = max(ans, dis[i])
        return ans + 1
            