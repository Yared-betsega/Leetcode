class Solution:
    def clumsy(self, n: int) -> int:
        op, queue, j = ["*", "/", "+", "-"], deque(), 0
        
        for i in range(n, 0, -1):
            j = 0 if j == len(op) else j
            queue.extend([i, op[j]])
            j += 1
            
        queue.pop()
        forAddAndSub = deque()
        firstPrecedence = set(["*", "/"])
        while len(queue) > 1:
            first = queue.popleft()
            operation = queue.popleft()
            if operation in firstPrecedence:
                second = queue.popleft()
                queue.appendleft(first * second) if operation == "*" else queue.appendleft(first//second)
            else:
                forAddAndSub.append(first)
                forAddAndSub.append(operation)
        
        forAddAndSub.append(queue[0])
        while len(forAddAndSub) > 1:
            first = forAddAndSub.popleft()
            operation = forAddAndSub.popleft()
            second = forAddAndSub.popleft()
            forAddAndSub.appendleft(first + second) if operation == "+" else forAddAndSub.appendleft(first - second)
    
        return forAddAndSub[0]

# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)
