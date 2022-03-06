# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def bfs(node):
            answer = []
            queue = deque([(node, None, 0)])
            
            while queue:
                cur, parent, length = queue.popleft()
                
                if cur.val == x or cur.val == y:
                    answer.append([parent, length])
                if cur.left:
                    queue.append((cur.left, cur, length + 1))
                if cur.right:
                    queue.append((cur.right, cur, length + 1))
        
            return answer
        
        get = bfs(root)        
        return True if get[0][0] != get[1][0] and get[0][1] == get[1][1] else False
                    
# time and space complexity 
# time coplexity = O(n)
# space complexity = O(n)
                
