class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        net = defaultdict(list)
        for i in range(len(arr)):
            net[arr[i]].append(i)
            
        # print(net)
        
        isValid = lambda index: 0 <= index <len(arr) and index not in self.visited
        
        self.visited = set()
        def bfs(start):
            
            queue = deque([(start, -1)])
            
            while queue:
                
                cur, length = queue.popleft()
                length += 1
                if cur == len(arr) - 1:
                    return length
                
                if isValid(cur+1):
                    queue.append((cur + 1, length))
                    
                if isValid(cur - 1):
                    queue.append((cur - 1, length))
                    
                if cur not in self.visited:
                    self.visited.add(cur)
                    temp = net[arr[cur]]
                    for jump in net[arr[cur]]:
                        if isValid(jump):
                            queue.append((jump, length))
                            self.visited.add(jump)
                        
        return bfs(0)
                    
                
                
            