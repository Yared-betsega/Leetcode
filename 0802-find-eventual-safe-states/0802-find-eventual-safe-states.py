class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = defaultdict(int)
        self.ans = 0
        inCycle = set()
        def topSort(node):
            if color[node] == 1:
                inCycle.add(node)
                return True
            if color[node] == 2:
                return False
            
            color[node] = 1
            
            for neigh in graph[node]:
                hasCycle = topSort(neigh)
                self.ans += hasCycle
                if hasCycle:
                    inCycle.add(node)
                    return True
            
            color[node] = 2
            return False
        for i in range(len(graph)):
            topSort(i)
            
        ans = []
        for i in range(len(graph)):
            if i not in inCycle:
                ans.append(i)
        return ans