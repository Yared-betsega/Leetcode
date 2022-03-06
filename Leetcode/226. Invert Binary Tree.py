# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(node):
            if not node:
                return 
            
            queue = deque([node])
            
            while queue:
                cur = queue.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
            return node
        
        return bfs(root)
    
# time and space complexity
# time complexity = O(n)
# space complexity = O(n)
