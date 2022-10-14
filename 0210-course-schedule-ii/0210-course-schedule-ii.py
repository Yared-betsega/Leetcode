class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        colors = [0] * numCourses
        def dfs(node, path):
            if colors[node] == 1:
                return True
            if colors[node] == 2:
                return False
            colors[node] = 1

            for neighbor in graph[node]:
                hasCycle = dfs(neighbor, path)
                if hasCycle:
                    return True
            colors[node] = 2
            self.answer.append(node)
            
        self.answer = []        
        for course in range(numCourses):
            hasCycle = dfs(course, set())
            if hasCycle:
                return []
                
        self.answer.reverse()
        return self.answer
    
# time and space complexity 
# time complexity = O(V+E)
# space complexity = O(V)
# v = number of vertices
# E = number of edges