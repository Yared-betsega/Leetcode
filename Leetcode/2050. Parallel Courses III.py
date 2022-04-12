
# https://leetcode.com/problems/parallel-courses-iii/
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        inDegrees = [0 for _ in range(n)]
        outDegree = defaultdict(set)
        
        for pre, course in relations:
            outDegree[pre].add(course)
            inDegrees[course-1] += 1
        
        queue = deque()
        for i in range(n):
            if inDegrees[i]==0:
                queue.append(i+1)
                
        shortest_time = time[:]
        while queue:
            course = queue.popleft()
            
            for neighbor in outDegree[course]:
                shortest_time[neighbor-1] = max(shortest_time[neighbor-1], shortest_time[course-1]+time[neighbor-1])
                inDegrees[neighbor-1] -= 1
                if inDegrees[neighbor-1]==0:
                    queue.append(neighbor)
                    
        return max(shortest_time)
