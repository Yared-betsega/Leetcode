# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(node):
            if not node:
                return
            
            level = []
            queue = deque([node])
            
            while queue:
                temp = []
                for i in range(len(queue)):
                    cur = queue.popleft()
                    temp.append(cur.val)
                    
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                        
                level.append(temp)
                
            return level
        
        answer = bfs(root)
        if answer:
            answer.reverse()
        return answer
