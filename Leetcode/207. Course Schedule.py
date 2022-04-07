# https://leetcode.com/problems/course-schedule/

# DFS Approach
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True
        
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        def dfs(node, path):
            path.add(node)
            self.visited.add(node)

            for neighbor in graph[node]:
                if neighbor in path:
                    self.hasCycle = True
                if neighbor not in self.visited:
                    dfs(neighbor, path)
                    
            path.remove(node)
            self.answer += 1

        self.answer = 0
        self.hasCycle = False
        self.visited = set()
        
        for course in range(numCourses):
            if course not in self.visited:
                dfs(course, set())
        
        return not self.hasCycle and self.answer == numCourses
                
# time and space complexity 
# time complexity = O(V+E)
# space complexity = O(V)
# v = len(vertices), e = len(edges)
                
                
