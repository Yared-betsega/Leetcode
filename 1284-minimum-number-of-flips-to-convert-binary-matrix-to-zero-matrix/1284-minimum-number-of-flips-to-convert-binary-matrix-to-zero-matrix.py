class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        pos = {}
        startState = i = 0
        graph = defaultdict(list)
        for row in range(n):
            for col in range(m):
                pos[(row, col)] = i
                graph[i - 1].append((row, col))
                mat[row][col] ^= 1
                if mat[row][col]:
                    startState |= 1 << i
                i += 1
        
        
        fullTurnedOn = (2 ** (n * m)) - 1 
        # print(fullTurnedOn)
        DIR = [(0,1), (0,-1), (-1,0), (1,0)]
        nxt = [(0,1), (1,0)]
        queue = deque([(0, 0, startState, 0)])
        
        isValid = lambda r, c: 0 <= r < n and 0 <= c < m 
        answer = float("inf")
        while queue:
            for _ in range(len(queue)):
                row, col, currentState, count = queue.popleft()
                if currentState == fullTurnedOn:
                    answer = min(answer, count)
                if currentState & (1 << pos[(row, col)]):
                    flippedState = currentState & (~(1 << pos[(row, col)]))
                else:
                    flippedState = currentState | (1 << pos[(row, col)])
                
                for dx, dy in DIR:
                    nx, ny = row + dx, col + dy
                    if isValid(nx, ny):
                        if flippedState & (1 << pos[(nx, ny)]):
                            flippedState = flippedState & (~(1 << pos[(nx, ny)]))
                        else:
                            flippedState = flippedState | (1 << pos[(nx, ny)])
                            
                # print(row, col, currentState, flippedState)
                if flippedState == fullTurnedOn:
                    answer = min(answer, count + 1)
                
                
                for nx, ny in graph[pos[(row, col)]]:
                    queue.append((nx, ny, flippedState, count + 1))
                    queue.append((nx, ny, currentState, count))
            
        
        return -1 if answer == float("inf") else answer
            
