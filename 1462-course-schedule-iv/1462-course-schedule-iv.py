class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for pre, course in prerequisites:
            graph[course].append(pre)
            indegree[pre] += 1
            
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        isReachable = defaultdict(set)
        
        while queue:
            currentCourse = queue.popleft()
            for pre in graph[currentCourse]:
                isReachable[pre].add(currentCourse)
                isReachable[pre].update(isReachable[currentCourse])
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)  
        answer = []
        for i, j in queries:
            answer.append(j in isReachable[i])
        
        return answer