class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        '''
        Color Definition:
            -1: Black (no cycle afterwards)
            0: white (First visit)
            otherwise: Grey (there is a cycle), The value represents the number of nodes previously visited.
        '''
        color = [0] * len(edges) # Initially all elements are not visited
        
        longestCycle = [-1] # intitialize longest cycle to be smallest value
        
        def topSort(node, preCount):
            if color[node] == -1: # No cycle afterwards so no value proceeding
                return False
            if color[node] != 0: # Has cycle, update the value of longest cycle to be the max of itself or the length of the current cycle
                longestCycle[0] = max(longestCycle[0], preCount - color[node])
                return True
            
            color[node] = preCount # Mark the current node to be visited
            if edges[node] != -1:
                hasCycle = topSort(edges[node], preCount + 1)
                if hasCycle:
                    return True
            
            color[node] = -1  # If no cycle, mark the node to black and return
            return False
        
        for i in range(len(edges)):
            topSort(i, 0)
        
        return longestCycle[0]
                