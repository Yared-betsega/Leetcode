# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        
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
            self.answer.append(node)

        self.answer = []
        self.hasCycle = False
        self.visited = set()
        
        for course in range(numCourses):
            if course not in self.visited:
                dfs(course, set())
                
        self.answer.reverse()
        return [] if self.hasCycle else self.answer
    
# time and space complexity 
# time complexity = O(V+E)
# space complexity = O(V)
# v = number of vertices
# E = number of edges
