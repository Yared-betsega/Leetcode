class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def isValid(index):
            return True if 0 <= index <len(arr) and index not in visited else False
        
        visited = set()
        queue = deque([start])
        
        while queue:
            cur = queue.popleft()
            
            if arr[cur] == 0:
                return True
            
            nextMove = cur + arr[cur]
            if isValid(nextMove):
                queue.append(nextMove)
                visited.add(nextMove)
            
            nextMove = cur - arr[cur]
            if isValid(nextMove):
                queue.append(nextMove)
                visited.add(nextMove)
        
        return False

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)
            
            
            
            
