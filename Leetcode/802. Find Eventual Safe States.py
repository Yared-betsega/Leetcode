# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
                
        def dfs(node):
            self.path.add(node)
            self.visited.add(node)
            for neighbor in graph[node]:
                if neighbor in self.path:
                    self.hasCycle.add(neighbor)
                    self.hasCycle.add(node)
                    return True
                if neighbor not in self.visited:
                    cond = dfs(neighbor)
                    if cond:
                        self.hasCycle.add(node)
                        return True
            
            self.path.remove(node) 
            return False
            

        self.hasCycle, self.visited, self.path = set(), set(), set()
        
        for course in range(len(graph)):
            if course not in self.visited:
                dfs(course)
                    
        return list(filter(lambda x:x not in self.hasCycle, range(len(graph))))
