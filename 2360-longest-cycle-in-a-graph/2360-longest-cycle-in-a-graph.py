class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        color = [0] * len(edges)
        longestCycle = [-1]
        
        def topSort(node, preCount):
            if color[node] == -1:
                return False
            if color[node] != 0:
                longestCycle[0] = max(longestCycle[0], preCount - color[node])
                return True
            color[node] = preCount
            if edges[node] != -1:
                hasCycle = topSort(edges[node], preCount + 1)
                if hasCycle:
                    return True
            
            color[node] = -1
            return False
        
        for i in range(len(edges)):
            topSort(i, 0)
        
        return longestCycle[0]
                