class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def bfs(node):
            if not node:
                return 
            queue = deque([node])
            
            while queue:
                
                n = len(queue)
                for i in range(n):
                    cur = queue.popleft()
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                        
                    if i + 1 < n:
                        cur.next = queue[0]
                    else:
                        cur.next = None
        bfs(root)
        return root