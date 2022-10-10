class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        reds = defaultdict(set)        
        for x, y in redEdges:
            reds[x].add(y)
            
        blues = defaultdict(set)
        for x, y in blueEdges:
            blues[x].add(y)
        
        ans = [float("inf")] * n
        level = 0
        queue = deque([(0, None)])
        redVisited = set()
        blueVisited = set()
        while queue:
            for i in range(len(queue)):
                cur, prevColor = queue.popleft()
                ans[cur] = min(ans[cur], level)
                if prevColor == "R" or prevColor == None:
                    for nxt in blues[cur]:
                        if nxt not in blueVisited:
                            queue.append((nxt, "B"))
                            blueVisited.add(nxt)
                if prevColor == "B" or prevColor == None:
                    for nxt in reds[cur]:
                        if nxt not in redVisited:
                            queue.append((nxt, "R"))
                            redVisited.add(nxt)
            level += 1
        
        for i in range(len(ans)):
            if ans[i] == float("inf"):
                ans[i] = -1
        return  ans
                

        