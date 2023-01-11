class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = defaultdict(int)
        self.ans = 0
        inCycle = set()
        def topSort(node):
            if color[node] == 1:
                return True
            if color[node] == 2:
                return False
            
            color[node] = 1
            
            for neigh in graph[node]:
                hasCycle = topSort(neigh)
                if hasCycle:
                    return True
            
            color[node] = 2
            return False
        for i in range(len(graph)):
            topSort(i)
            
        ans = []
        for i in range(len(graph)):
            if color[i] == 2:
                ans.append(i)
        return ans